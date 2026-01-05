<p align="center">
  <img src="https://github.com/ferrumc-rs/ferrumc/blob/master/assets/README/header.svg?raw=true" alt="FerrumC Header" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/ferrumc-rs/ferrumc?style=for-the-badge&color=red" alt="License">
  <img src="https://img.shields.io/github/languages/code-size/ferrumc-rs/dashboard?style=for-the-badge&color=red" alt="Code Size">
  <img src="https://img.shields.io/badge/Sveltekit-FF3E00?style=for-the-badge&color=red" alt="SvelteKit">
  <a href="https://discord.gg/qT5J8EMjwk">
    <img src="https://img.shields.io/discord/1277314213878173726?style=for-the-badge&logo=discord&logoColor=red&color=red" alt="Discord">
  </a>
</p>

---

### ⚡ Integrated by Default
> [!IMPORTANT]
> **No installation needed.** This dashboard is natively served by the [FerrumC](https://github.com/ferrumc-rs/ferrumc) Rust binary. This repo is only for UI development and contribution.

---

## ✨ Features

- 🛰️ **Real-time:** Persistent bi-directional WebSocket connection.
- 📊 **Live Stats:** Instant server metrics, logs, and player counts.
- 🎮 **Remote Console:** Full command execution from your browser.
- 📱 **Responsive:** Fully optimized for Mobile and Desktop management.

---

## 🖼️ Gallery

<div align="center">
  <table border="0">
    <tr style="border: none;">
      <td width="79%" align="center" style="border: none; vertical-align: bottom;">
        <p><b>Desktop Interface</b></p>
        <img src="https://github.com/ferrumc-rs/dashboard/blob/master/assets/README/FerrumC%20Dashboard.png?raw=true" width="100%" style="border-radius: 10px;" alt="FerrumC Desktop Dashboard">
      </td>
      <td width="21%" align="center" style="border: none; vertical-align: bottom;">
        <p><b>Mobile</b></p>
        <img src="https://github.com/ferrumc-rs/dashboard/blob/master/assets/README/FerrumC%20Dashboard%20Mobile.png?raw=true" width="100%" style="border-radius: 10px;" alt="FerrumC Mobile Dashboard">
      </td>
    </tr>
  </table>
</div>

---

## 🛠️ Developer Quickstart

If you want to contribute to the UI or run a custom dev environment:

```bash
# 1. Setup
pnpm i

# 2. Run Dev (Connects to local FerrumC)
pnpm dev

# 3. Build (Outputs to ./build)
pnpm build
```

[!TIP]

To link to a specific instance: localhost:5173/?ws_port=9000

🔄 Automated Workflow

Commit: Push changes to master.

CI/CD: GitHub Actions bundles the SvelteKit app.

Deploy: Artifacts are uploaded to Releases.

Sync: FerrumC binary automatically fetches and serves the latest UI.

<p align="center">

Built with ❤️ by the <b>FerrumC Team</b> • <a href="https://discord.gg/qT5J8EMjwk">Join Discord</a>

</p>