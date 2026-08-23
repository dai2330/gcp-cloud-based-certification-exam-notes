# Getting Started with Google Kubernetes Engine 課程頁設計

## 目標

將 `ACE_Getting_Started_with_Google_Kubernetes_Engine.md` 納入 ACE 筆記網站，在 `Google Kubernetes Engine` 系列下建立一門課一頁的閱讀頁面。

## 內容與路徑

- 新頁：`docs/courses/ace/google-kubernetes-engine/getting-started-with-google-kubernetes-engine.md`
- 標題：`Getting Started with Google Kubernetes Engine`
- 保留全部正文、表格、命令、Bash 註解、Mermaid 與連結的原順序。
- 只調整 fenced code 外的 Markdown 標題：課名為唯一 H1；六個 Chapter 與 ACE 統整為 H2；內層標題依序下移。

## 導覽與驗收

- 在 Associate Cloud Engineer 下新增 `Google Kubernetes Engine` 系列，排在 Elastic 系列後。
- 首頁加入第四張課程卡與路徑節點；ACE 學習路線加入第 4 門課。
- 測試需驗證 392 行來源的非標題內容順序、Bash `#` 註解仍位於 code fence、唯一頁面 H1、六個 Chapter、兩張 Mermaid 與所有入口。
- 全套測試、嚴格建置、GitHub Actions 及公開 HTTP 驗證均需成功。
