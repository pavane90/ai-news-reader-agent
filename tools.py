import time
from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

search_tool = SerperDevTool(
    n_results=30,
)

@tool
def scrape_tool(url: str):
    """
    Use this when you need to read the content of a website.
    Returns the content of a website, in case the website is not available, it returns 'No content'.
    Input should be a `url` string. for example (https://www.reuters.com/world/asia-pacific/cambodia-thailand-begin-talks-malaysia-amid-fragile-ceasefire-2025-08-04/)
    """

    print(f"Scrapping URL: {url}")

    with sync_playwright() as p:
        # 브라우저로 창없이 백그라운드에서 실행
        browser = p.chromium.launch(headless=True)

        # 새 페이지 작성
        page = browser.new_page()

        # 원하는 url로 접속
        page.goto(url)

        # 5초정도 멈추게 하고 로딩
        time.sleep(5)

        # html추출
        html = page.content()

        # 브라우저 닫기
        browser.close()

        # HTML을 작성하고 조작하는 beautifulsoup객체 작성
        soup = BeautifulSoup(html, "html.parser")
        
        # 불필요한 태그 제거, 이 태그에는 필요한 내용이 없음
        unwanted_tags = [
            "header",
            "footer",
            "nav",
            "aside",
            "script",
            "style",
            "noscript",
            "iframe",
            "form",
            "button",
            "input",
            "select",
            "textarea",
            "img",
            "svg",
            "canvas",
            "audio",
            "video",
            "embed",
            "object",
        ]

        # 불필요한 태그 제거 (decompose)
        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        # 페이지 요소안에 있는 모든 자식 content반환, 텍스트만
        content = soup.get_text(separator=" ")

        # scrape_tool에서 불필요한거 반환하지 마라 했으므로 
        # 내용이 없다면 No content반환
        return content if content != "" else "No content"