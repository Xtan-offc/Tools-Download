
cat > socialdl.py <<'PY'
import os
import sys
import shutil
import subprocess

OUT = os.path.expanduser(
    "~/storage/downloads/SocialDownloader"
)

os.makedirs(OUT, exist_ok=True)

def banner():
    os.system("clear")
    print("=" * 42)
    print("       XTAN SOCIAL DOWNLOADER")
    print("          Powered by Xtan")
    print("=" * 42)
    print("  1. Download video (MP4)")
    print("  2. Download audio (MP3)")
    print("  3. Lihat folder hasil download")
    print("  4. Keluar")
    print("=" * 42)

def download(mode):
    url = input("\nMasukkan URL media: ").strip()

    if not url.startswith(("https://", "http://")):
        print("[!] URL tidak valid.")
        input("Enter untuk kembali...")
        return

    if mode == "video":
        options = [
            "yt-dlp",
            "--no-playlist",
            "-f", "bv*+ba/b",
            "--merge-output-format", "mp4",
            "-o", os.path.join(OUT, "%(title).150s.%(ext)s"),
            url
        ]
    else:
        options = [
            "yt-dlp",
            "--no-playlist",
            "-f", "ba/b",
            "-x",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", os.path.join(OUT, "%(title).150s.%(ext)s"),
            url
        ]

    print("\n[*] Memulai proses download...\n")

    try:
        result = subprocess.run(options)
        if result.returncode == 0:
            print("\n[+] Proses selesai.")
            print("[+] Folder:", OUT)
        else:
            print("\n[!] Download gagal.")
            print("Periksa URL, koneksi, atau dukungan situs.")
    except FileNotFoundError:
        print("[!] yt-dlp belum terpasang.")
    except KeyboardInterrupt:
        print("\n[!] Download dibatalkan.")

    input("\nTekan Enter untuk kembali...")

def main():
    while True:
        banner()
        choice = input("Pilih menu > ").strip()

        if choice == "1":
            download("video")
        elif choice == "2":
            download("audio")
        elif choice == "3":
            print("\nLokasi:", OUT)
            if os.path.isdir(OUT):
                files = os.listdir(OUT)
                if files:
                    for name in files:
                        print(" -", name)
                else:
                    print("Folder masih kosong.")
            input("\nTekan Enter untuk kembali...")
        elif choice == "4":
            print("XTAN SOCIAL DOWNLOADER - Bye!")
            break
        else:
            input("Pilihan tidak valid. Enter untuk kembali...")

if __name__ == "__main__":
    if shutil.which("yt-dlp") is None:
        print("Install dahulu: pip install -U yt-dlp")
        sys.exit(1)
    main()
PY
                               
