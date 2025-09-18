# AI NEWS READER AGENT

## .env파일 구성

OPENAI_API_KEY="openai-api-key"
SERPER_API_KEY="serper-api-key"

- OPENAI_API_KEY 발생

[이 URL](https://platform.openai.com/settings/organization/usage)에서 키를 발급받은뒤 사용. 테스트는 gpt-4o-mini (기본값)

- LLM버전 변경

[이 URL](https://docs.crewai.com/en/learn/llm-connections)의 절차를 참고

- 실행

main.py

```
result = NewsReaderAgent().crew().kickoff(inputs={"topic": "여기에 주제를 입력"})
```

```terminal
uv sync
uv run main.py
```
