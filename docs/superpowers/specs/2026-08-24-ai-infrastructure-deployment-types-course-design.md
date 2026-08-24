# AI Infrastructure: Deployment Types 課程頁設計

## 目標

將 `ACE_AI_Infrastructure_Deployment_Types.md` 納入 ACE 筆記網站，在既有 `AI Infrastructure` 系列下建立 Deployment Types 單頁並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/ai-infrastructure/ai-infrastructure-deployment-types.md`
- 標題：`AI Infrastructure: Deployment Types`
- 保留全部正文、表格、命令、程式碼註解、Mermaid 與連結原順序。
- 只調整 fenced code 外標題：課名為唯一 H1；三個 Chapter 與認證重點統整為 H2；內層標題依序下移。

## 導覽與呈現

- 在既有 `AI Infrastructure` 系列中新增 `Deployment Types`，排在 `Cloud TPUs` 後。
- 首頁加入第十張課程卡與第十個路徑節點；ACE 學習路線加入第 10 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 633 行來源、唯一 H1、三個 Chapter、四張 Mermaid、五個 Bash 程式碼註解及所有入口。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200 並包含課程標題與核心章節。
