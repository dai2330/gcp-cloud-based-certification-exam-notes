# GSP313 Implement Load Balancing on Compute Engine Challenge Lab 課程頁設計

## 目標

將 `ACE_GSP313_Implement_Load_Balancing_on_Compute_Engine_Challenge_Lab.md` 納入 ACE 筆記網站，建立新的 `Implement Load Balancing on Compute Engine` 課程系列與 GSP313 Challenge Lab 獨立單頁，並部署至 GitHub Pages。

## 內容與路徑

- 新頁：`docs/courses/ace/implement-load-balancing-on-compute-engine/implement-load-balancing-on-compute-engine-challenge-lab.md`
- 標題：`Implement Load Balancing on Compute Engine: Challenge Lab (GSP313)`
- 保留全部正文、表格、命令、純文字輸出、Mermaid 與連結原順序。
- 將第一個 H1 正規化為課名，第二個 H1 `認證重點統整` 降為 H2；其餘 H2/H3/H4 與 fenced code 保持原樣。

## 導覽與呈現

- 在 Associate Cloud Engineer 下新增 `Implement Load Balancing on Compute Engine` 系列，排在 Terraform 系列後，子項標示為 `Challenge Lab (GSP313)`。
- 首頁加入第十三張課程卡與第十三個路徑節點；ACE 學習路線加入第 13 門課。
- 沿用目前 MkDocs Material 版型、響應式版面、搜尋與 Mermaid 呈現，不新增相依套件。

## 驗收

- 測試以 UTF-8 驗證 762 行來源、唯一 H1、13 個編號 H2、`認證重點統整` H2、30 個 H3、5 個 H4、2 張 Mermaid、28 個 Bash 與 5 個 text 區塊。
- 全套測試、嚴格建置、暫存差異、產物內容與敏感資訊掃描均需成功。
- GitHub Actions 部署成功後，公開課程頁及首頁皆須回傳 HTTP 200，並包含 GSP313、Network Load Balancer 與 Application Load Balancer 核心內容。
