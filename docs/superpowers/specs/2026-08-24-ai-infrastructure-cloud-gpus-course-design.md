# AI Infrastructure: Cloud GPUs 課程頁設計

## 目標

將 `ACE_AI_Infrastructure_Cloud_GPUs.md` 納入 ACE 筆記網站，在新的 `AI Infrastructure` 系列下建立 Cloud GPUs 單頁並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/ai-infrastructure/ai-infrastructure-cloud-gpus.md`
- 標題：`AI Infrastructure: Cloud GPUs`
- 保留全部正文、表格、命令、程式碼註解、Mermaid 與連結原順序。
- 只調整 fenced code 外標題：課名為唯一 H1；三個 Chapter 與認證重點統整為 H2；內層標題依序下移。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增 `AI Infrastructure` 系列，排在 Google Cloud Databases 後，子項名稱為 `Cloud GPUs`。
- 首頁加入第八張課程卡與第八個路徑節點；ACE 學習路線加入第 8 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 586 行來源、唯一 H1、三個 Chapter、三張 Mermaid、程式碼內 `#` 註解及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與核心章節。
