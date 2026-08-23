# Scaling and Automation 課程頁設計

## 目標

將 `ACE_Elastic_Google_Cloud_Infrastructure_Scaling_and_Automation.md` 納入既有 Google Cloud ACE 筆記網站，建立 `Elastic Google Cloud Infrastructure` 課程系列，維持一門課一個完整網頁。

## 內容與路徑

- 新頁：`docs/courses/ace/elastic-google-cloud-infrastructure/elastic-google-cloud-infrastructure-scaling-and-automation.md`
- 標題：`Elastic Google Cloud Infrastructure: Scaling and Automation`
- 原始正文、表格、程式碼、Mermaid 與來源連結完整保留並維持順序。
- 只正規化標題：課程名稱為唯一 H1；五個 Chapter 與認證重點統整為 H2；其下標題依序下移。

## 導覽與呈現

- `mkdocs.yml` 在 Associate Cloud Engineer 下新增 `Elastic Google Cloud Infrastructure` 系列，排在 Essential 系列之後。
- 首頁新增第三張課程卡與學習路徑節點。
- ACE 學習路線新增第 3 門課，不拆分 Chapter、不變更既有視覺樣式。

## 驗收

- 測試先證明頁面與導覽不存在，再驗證路徑、唯一 H1、五個 Chapter、821 行來源的非標題內容順序及所有導覽入口。
- 全套測試與 `mkdocs build --strict` 必須通過。
- 推送後 GitHub Actions 必須成功，公開課程網址需回傳 HTTP 200 並包含課程標題與核心章節。
