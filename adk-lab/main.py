"""Google Cloud Day Taipei '26 — Build Multi-Agent Systems with ADK
Three Workflow Agent Patterns: Sequential, Parallel, Loop
"""
from google.adk import Agent, Workflow

# ============================================================
# 1. SEQUENTIAL AGENT — 線性依序執行
# ============================================================

extract_agent = Agent(
    name="extract_agent",
    model="gemini-2.5-flash",
    instruction="Extract the key topics from the user query. Return only the topics as a comma-separated list.",
)

analyze_agent = Agent(
    name="analyze_agent",
    model="gemini-2.5-flash",
    instruction="Analyze the given topics and provide a brief summary of each.",
)

summarize_agent = Agent(
    name="summarize_agent",
    model="gemini-2.5-flash",
    instruction="Combine the analysis into a final structured report.",
)

sequential_workflow = Workflow(
    name="sequential_workflow",
    description="Extract → Analyze → Summarize (sequential pipeline)",
    edges=[
        ("START", extract_agent, analyze_agent),
        (analyze_agent, summarize_agent, "END"),
    ],
)

# ============================================================
# 2. PARALLEL AGENT — 多路並行執行
# ============================================================

market_agent = Agent(
    name="market_agent",
    model="gemini-2.5-flash",
    instruction="Analyze the market trends for the given topic. Return a market analysis report.",
)

tech_agent = Agent(
    name="tech_agent",
    model="gemini-2.5-flash",
    instruction="Analyze the technical aspects of the given topic. Return a technical analysis report.",
)

risk_agent = Agent(
    name="risk_agent",
    model="gemini-2.5-flash",
    instruction="Identify the risks and challenges for the given topic. Return a risk assessment report.",
)

parallel_workflow = Workflow(
    name="parallel_workflow",
    description="Market + Tech + Risk analysis in parallel",
    edges=[
        ("START", market_agent, "END"),
        ("START", tech_agent, "END"),
        ("START", risk_agent, "END"),
    ],
)

# ============================================================
# 3. LOOP AGENT — 反覆迭代直到滿足條件
# ============================================================

draft_agent = Agent(
    name="draft_agent",
    model="gemini-2.5-flash",
    instruction="Draft a solution for the given problem.",
)

review_agent = Agent(
    name="review_agent",
    model="gemini-2.5-flash",
    instruction="""Review the solution and identify issues.
If the solution is satisfactory, respond with exactly: 'QUALITY_PASS'
Otherwise, list specific improvements needed.""",
)

fix_agent = Agent(
    name="fix_agent",
    model="gemini-2.5-flash",
    instruction="Apply the review feedback to improve the solution. Return the improved version.",
)

loop_workflow = Workflow(
    name="loop_workflow",
    description="Draft → Review → Fix (loop until quality pass, max 3 iterations)",
    edges=[
        ("START", draft_agent, review_agent),
        (review_agent, fix_agent, review_agent),   # loop back
        (review_agent, "END"),                       # exit on quality pass
    ],
)

# ============================================================
# Root Agent — 入口
# ============================================================

root_agent = Agent(
    name="multi_agent_system",
    model="gemini-2.5-flash",
    instruction="""You are a multi-agent orchestration system.
Route user requests to the appropriate workflow:
- Sequential: step-by-step processing pipeline
- Parallel: concurrent analysis from multiple perspectives
- Loop: iterative refinement until quality is met""",
)

if __name__ == "__main__":
    print("ADK Multi-Agent System Ready")
    print("Workflows: sequential_workflow, parallel_workflow, loop_workflow")
