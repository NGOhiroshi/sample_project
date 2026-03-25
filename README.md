# Dev Containerでの開発環境テンプレート

## Dev Container立ち上げ手順

### 前提条件

Dev Containerを使用するには、以下のソフトウェアをインストールしてください：

- **コンテナエンジン（以下のいずれか）**
  - **OrbStack** (推奨 - Mac/Linux)
    - [OrbStack公式サイト](https://orbstack.dev/) からダウンロード
  - **Docker Desktop** (Windows/Mac) 
    - [Docker Desktop公式サイト](https://www.docker.com/products/docker-desktop/) からダウンロード
  - **Docker Engine** (Linux)
  - バージョン: 20.10以上
  
- **Visual Studio Code**
  - バージョン: 1.86以上
  
- **Dev Containers拡張機能**
  - VS Code内で `ms-vscode-remote.remote-containers` をインストールする

### セットアップ手順

#### 1. リポジトリのクローン

```bash
git clone <repository-url>
cd sample_project
```

#### 2. VS Codeでフォルダを開く

```bash
code .
```

#### 3. Dev Containerで開く

以下のいずれかの方法で開きます：

**方法1: コマンドパレットを使用（推奨）**
- `Ctrl+Shift+P` (Windows/Linux) または `Cmd+Shift+P` (Mac) を押す
- 「Dev Containers: Reopen in Container」を検索して実行
- 初回は数分かかります

**方法2: クイックアクションから開く**
- VS Codeの左下にある「><」アイコンをクリック
- 「Dev Containers: Reopen in Container」を選択

#### 4. コンテナの起動確認

コマンドパレット内に以下の表示が確認できたら成功です：
```
[dev container] Starting Dev Container
[dev container] Dev container running...
```

#### 5. devcontainer.jsonを更新した場合

`devcontainer.json` や `requirements.txt` など、コンテナ設定を更新した場合は、以下の手順でイメージを再ビルドしてください：

**方法1: コマンドパレットを使用（推奨）**
- `Ctrl+Shift+P` (Windows/Linux) または `Cmd+Shift+P` (Mac) を押す
- 「Dev Containers: Rebuild Container」を検索して実行

**方法2: クイックアクションから再ビルド**
- VS Codeの左下にある「><」アイコンをクリック
- 「Dev Containers: Rebuild Container」を選択

**重要:** `postCreateCommand` の変更は再ビルドが必須です。そうしなければ新しい依存関係がインストールされません。

### よく使うコマンド

```bash
# Dockerコンテナのビルド（手動で必要な場合）
# プロジェクト内に .devcontainer/devcontainer.json がある場合自動で実行されます

# コンテナ内でのシェルセッションを開く
# VS Code内で integrated terminal を開く (Ctrl+`)

# Dockerイメージ一覧の確認
docker images | grep vscode

# 既存のコンテナを停止・削除
docker ps -a  # コンテナ一覧確認
docker stop <container-id>
docker rm <container-id>
```

### ファイル構造

```
.devcontainer/
├── devcontainer.json    # Dev Container設定ファイル
└── Dockerfile          # コンテナイメージの定義（必要に応じて）
```

### トラブルシューティング

**問題: 「Dev Containers」拡張機能が見つからない**
- 解決策: VS Code Extensions (Ctrl+Shift+X) から `ms-vscode-remote.remote-containers` をインストール

**問題: Dockerが起動していない**
- 解決策: Docker Desktop/Engineを起動してください
- 確認コマンド: `docker ps`

**問題: コンテナのビルドに失敗する**
- 解決策: 
  - `.devcontainer/devcontainer.json` の設定を確認
  - `docker system prune` でクリーンアップ
  - 「Dev Containers: Rebuild Container」で再ビルド

**問題: requirements.txtを更新したが、パッケージがインストールされていない**
- 解決策:
  - `.devcontainer/devcontainer.json` が `postCreateCommand` を設定していることを確認
  - 「Dev Containers: Rebuild Container」で再ビルド

**問題: ポート番号の競合**
- 解決策: `.devcontainer/devcontainer.json` 内の `forwardPorts` を別のポート番号に変更

### 環境情報

- **ホストOS**: Linux (Debian Trixie)
- **Node.js**: プリインストール済み
- **Python**: Python 3 / pip3 プリインストール済み
- **Git**: ビルド済み最新版プリインストール済み
- **ESLint**: Node.js開発用プリインストール済み

### 参考リンク

- [Visual Studio Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Docker Documentation](https://docs.docker.com/)
- [Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
