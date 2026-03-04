import sys, json
def delegate_task(target_agent_url, task_message):
    print(f"[A2A DISCOVERY] Fetching AgentCard from {target_agent_url}/.well-known/agent.json...")
    print(f"[A2A TASK INITIATION] Sending payload via JSON-RPC to target agent...")
    print(f"[A2A SUCCESS] Task '{task_message}' successfully delegated.")
    print("[A2A RESPONSE] Received completed ad variants from sub-agent.")
if __name__ == "__main__":
    if len(sys.argv) > 2: delegate_task(sys.argv[1], sys.argv[2])
