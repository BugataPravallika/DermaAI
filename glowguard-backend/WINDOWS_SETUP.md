# GlowGuard Backend - Windows Setup Guide

## What's the Issue?

Your Windows PowerShell is returning "ERROR: Operation cancelled by user" when running pip install commands. This is likely a system configuration or terminal stdin issue.

## ✅ Solution - Manual Installation Steps

### Step 1: Open Command Prompt (cmd.exe) Instead of PowerShell

PowerShell has an issue with pip in this environment. Let's use `cmd.exe` instead:

```bash
# Press Win + R, type: cmd
# Then navigate to the project:
cd C:\Users\Admin\Desktop\AI-skincare\glowguard-backend
```

### Step 2: Activate Virtual Environment in CMD

```batch
venv\Scripts\activate.bat
```

You should see `(venv)` at the beginning of your command prompt.

### Step 3: Install Core Packages (One at a Time)

Install these packages individually:

```batch
python -m pip install fastapi
python -m pip install uvicorn
python -m pip install pydantic
python -m pip install python-dotenv
python -m pip install sqlalchemy
python -m pip install bcrypt
python -m pip install pyjwt
python -m pip install python-multipart
python -m pip install pillow
python -m pip install numpy
python -m pip install aiofiles
python -m pip install requests
```

### Step 4: Verify Installation

```batch
python -c "import fastapi; print('FastAPI installed!')"
```

### Step 5: Run the Backend Server

```batch
python main.py
```

The server should start at `http://localhost:8000`

---

## 🔄 Alternative: Using requirements-minimal.txt

If you want to install from a file in cmd.exe:

```batch
venv\Scripts\activate.bat
pip install -r requirements-minimal.txt
```

---

## 🚨 If Still Having Issues

### Problem: "Operation cancelled by user"

**Solutions to try:**

1. **Disable pip version check:**
   ```batch
   python -m pip install --disable-pip-version-check --no-input fastapi
   ```

2. **Use older pip version:**
   ```batch
   python -m pip install --upgrade pip==24.2
   python -m pip install -r requirements-minimal.txt
   ```

3. **Try with --user flag:**
   ```batch
   python -m pip install --user fastapi
   ```

4. **Clear pip cache:**
   ```batch
   python -m pip cache purge
   python -m pip install fastapi
   ```

---

## 📱 Complete Installation Sequence (Copy & Paste)

Open **Command Prompt** and paste this entire block:

```batch
cd C:\Users\Admin\Desktop\AI-skincare\glowguard-backend
venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pydantic python-dotenv sqlalchemy bcrypt pyjwt python-multipart pillow numpy aiofiles requests
python -c "import fastapi; print('Installation successful!')"
python main.py
```

---

## ✅ What to Do Next

Once your packages are installed:

1. Server runs at: `http://localhost:8000`
2. API docs at: `http://localhost:8000/docs`
3. To stop: Press `Ctrl+C`

Now set up the frontend in a different terminal:

```bash
cd C:\Users\Admin\Desktop\AI-skincare\glowguard-frontend
npm install
npm run dev
```

---

## 📋 Minimum Packages Needed (if trying to minimize)

For a basic running server:
```batch
python -m pip install fastapi uvicorn python-dotenv pydantic sqlalchemy
```

The ML/image processing packages can be installed later when needed.

---

## 🆘 Quick Troubleshooting

| Error | Solution |
|-------|----------|
| `"source" not recognized` (macOS/Linux command in PowerShell) | Use `venv\Scripts\activate.bat` instead |
| `ExecutionPolicy` error | Use **cmd.exe** instead of **PowerShell** |
| `No module named 'fastapi'` | Make sure venv is activated before importing |
| `pip: error: command was cancelled` | Try using cmd.exe and disable pip version check |

---

## 📞 Need More Help?

See the main README:
- [README.md](README.md)
- [QUICK_START.md](../QUICK_START.md)

---

**Remember:** Use **cmd.exe** (Command Prompt), not PowerShell!
