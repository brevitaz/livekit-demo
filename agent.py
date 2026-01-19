import logging

from livekit.agents import JobContext, cli, Agent, AgentSession, function_tool, WorkerOptions
from livekit.plugins import silero, azure, groq, openai, liveavatar

from livekit.plugins.turn_detector.multilingual import MultilingualModel

from config import Config
from utils.prompt_manager import PromptManager

logger = logging.getLogger("tool-calling")
logger.setLevel(logging.INFO)


# create tool calling agent class
class ToolCallingAgent(Agent):
    def __init__(self) -> None:
        get_prompt = PromptManager().get_prompt
        super().__init__(
            instructions=get_prompt("system_prompt", "default tool calling agent system prompt"),
        )

    @function_tool(
        name="Add_two_numbers",
        description="Use this tool to add two integers together and return the result.",
    )
    async def add(self, a: int, b: int) -> int:
        logger.info(f"Adding two numbers using tool: {a} + {b}")
        return a + b

async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}
    session = AgentSession(
        turn_detection=MultilingualModel(),
        stt=azure.STT(
            speech_key=Config.AZURE_SPEECH_KEY,
            speech_region=Config.AZURE_SPEECH_REGION,
            language="en-IN"
        ),
        tts=azure.TTS(
            speech_key=Config.AZURE_SPEECH_KEY,
            speech_region=Config.AZURE_SPEECH_REGION,
            voice=Config.AZURE_VOICE,
        ),
        llm=openai.LLM(
            model=Config.LLM_MODEL,
            temperature=float(Config.LLM_TEMPERATURE),
        ),
        # if want to use groq
        # llm=groq.LLM(
        #     model=Config.GROQ_LLM_MODEL,
        #     temperature=float(Config.LLM_TEMPERATURE),
        # ),
        vad=silero.VAD.load(
            sample_rate=16000,
        ),
        user_away_timeout=float(Config.USER_AWAY_TIMEOUT),
        min_interruption_duration=1.0,
    )

    avatar = liveavatar.AvatarSession(
        avatar_id=Config.LIVE_AVATAR_ID,  # ID of the LiveAvatar avatar to use
    )
    await avatar.start(session, room=ctx.room)

    await session.start(agent=ToolCallingAgent(), room=ctx.room)
    await ctx.connect()


if __name__ == "__main__":
    options: WorkerOptions = WorkerOptions(entrypoint_fnc=entrypoint, port=8005)
    cli.run_app(options)
