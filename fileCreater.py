from pathlib import Path

# ===================== 設定ここから =====================

# コンテスト名のプレフィックス
# 例: "ABC", "ARC", "AGC" など
CONTEST_PREFIX = "ABC"

# 問題番号（フォルダ番号）の終了値
# 001 ～ END_NUM まで作成されます
END_NUM = 500

# アルファベット部分の最後の文字
# 例: "G" にすると A ～ G まで作成 (A, B, C, D, E, F, G)
LAST_LETTER = "G"

# 既に存在するファイルをそのまま残したいなら True（中身を消したくない）
# 毎回「空ファイル」にリセットしたいなら False
SKIP_IF_EXISTS = True

# 数字部分は必ず 3 桁（001, 002, ...）なので固定
NUMBER_WIDTH = 3  # 基本的に変更不要

# ===================== 設定ここまで =====================


def main():
    # カレントディレクトリ固定
    base_dir = Path(".").resolve()
    print(f"作成先フォルダ: {base_dir}")

    # A ～ LAST_LETTER までの文字リストを作成
    try:
        letters = [chr(c) for c in range(ord("A"), ord(LAST_LETTER) + 1)]
    except Exception:
        raise ValueError("LAST_LETTER の設定がおかしいです（例: 'G' などの英大文字にしてください）。")

    if END_NUM < 1:
        raise ValueError("END_NUM は 1 以上にしてください。")

    for n in range(1, END_NUM + 1):  # 001 から END_NUM まで
        contest_id = f"{CONTEST_PREFIX}{n:0{NUMBER_WIDTH}d}"  # 例: ABC001, ABC002, ...
        contest_dir = base_dir / contest_id

        # フォルダ作成（既にあればスキップ）
        contest_dir.mkdir(parents=True, exist_ok=True)

        for letter in letters:
            file_name = f"{contest_id}{letter}.py"  # 例: ABC001A.py
            file_path = contest_dir / file_name

            if SKIP_IF_EXISTS and file_path.exists():
                # 既存ファイルは触らない
                continue

            # 常に空ファイルを作る（既にあれば中身を空にする）
            with file_path.open("w", encoding="utf-8"):
                pass

    print("作成完了！")


if __name__ == "__main__":
    main()
