# AI-App-Backend

## Links
- **Live Demo**: [https://igolas0.github.io/](https://igolas0.github.io/)
- **Frontend Repository**: [https://github.com/igolas0/igolas0.github.io](https://github.com/igolas0/igolas0.github.io)

## Overview
Simple AI chatbot backend using Hugging Face's free LLM API (Mistral-7B) and hosted on PythonAnywhere's free tier.

---
## Steps for deployment
## Step 1: Hugging Face Setup

### 1.1 Get Free LLM API Access
1. Sign up at [Hugging Face](https://huggingface.co)
2. Create API token:
   - Go to **Settings → Access Tokens → New Token**
   - Set Role: *Read*
3. Save token securely (used in backend configuration)

**Model Used**: `mistralai/Mistral-7B-Instruct-v0.2`

---

## Step 2: PythonAnywhere Deployment

### 2.1 Initial Setup
1. Create account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload repository files:
   - Go to **Files** tab → Upload project files

### 2.2 Configure Web App
1. Create Flask app:
   - **Web** tab → **Add a new web app**
   - Select *Flask* and *Python 3.10*

2. Set paths:
   ```plaintext
   Source code: /home/yourusername/path_to_project_files
   Working directory: Same as source code
    Update WSGI File (for path use the path where u dropped your files)

3. Update WSGI File  
3.1 **Open the auto-generated WSGI file** (via the **Web** tab).  
3.2 **Replace its contents** with:  
   ```python  
   import sys  
   path = '/home/yourusername/health-chatbot/backend'  
   if path not in sys.path:  
       sys.path.append(path)  
   from app import app as application  

4. Set Environment Variable
   ```plaintext
   In PythonAnywhere → **Web** tab → **Environment variables**:  
   HF_TOKEN=your_huggingface_token_here


5. Install Dependencies

   ```plaintext
   Open a Bash console and run:
   ```bash
   pip install flask flask-cors requests

6. Reload App

   ```plaintext
   Click the green Reload button in the Web tab.

# Technology Stack
- **Framework**: [Flask](https://flask.palletsprojects.com/) (Python) for lightweight API development.  
- **LLM Provider**: [Hugging Face Inference API](https://huggingface.co/inference-api) (Mistral-7B model).  
- **Hosting**: [PythonAnywhere](https://www.pythonanywhere.com) (free tier for deployment).  
- **Dependencies**:  
  - `flask-cors`: Enables cross-origin resource sharing.  
  - `requests`: Manages HTTP calls to Hugging Face’s API.  

---

## Key Features
- **Security**: Uses environment variables to store the Hugging Face API token securely.  
- **Scalability**: Stateless design allows horizontal scaling (upgrade for production workloads).  
- **Simplicity**: Minimal setup with <100 lines of core logic.  

---

## Workflow
1. User query → Frontend → Backend (`/chat` endpoint).  
2. Backend → Hugging Face API → Response sanitization.  
3. Sanitized response → Frontend → User.  
