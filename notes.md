You **cannot directly trigger a GitHub Actions workflow on a remote repository from your local CLI** using native GitHub CLI commands or tools. However, you can achieve this using the **GitHub API** or **GitHub CLI (`gh`)**, which allows you to trigger workflows remotely.

---

### **Using `gh` CLI to Trigger a Workflow**

1. **Install the GitHub CLI (`gh`)**:
   - Follow the installation guide for your platform: [GitHub CLI installation](https://cli.github.com/).

2. **Authenticate the CLI**:
   Run:
   ```bash
   gh auth login
   ```
   - Authenticate with your GitHub account.
   - Make sure you have the required permissions to manage workflows on the repository.

3. **Find the Workflow Name or ID**:
   List all workflows for your repository:
   ```bash
   gh workflow list
   ```
   This will show a list of workflows along with their names and IDs.

4. **Trigger the Workflow**:
   Use the following command to manually trigger the workflow:
   ```bash
   gh workflow run <workflow.yml>
   ```
   Replace `<workflow.yml>` with the filename or ID of the workflow you want to run (e.g., `update_readme.yml`).

   - To pass inputs (if the workflow uses `workflow_dispatch` with inputs):
     ```bash
     gh workflow run <workflow.yml> --field key=value
     ```

---

Raymond C. Turner

5. **Check the Workflow Status**:
   After triggering the workflow, you can monitor its status:
   ```bash
   gh run list
   gh run view <run-id>
   ```

---

### **Using cURL and GitHub API**

Alternatively, you can use the GitHub API to trigger a workflow remotely:

1. **Generate a Personal Access Token**:
   - Go to **Settings** > **Developer settings** > **Personal access tokens**.
   - Generate a token with `workflow` and `repo` permissions.

2. **Trigger the Workflow**:
   Use `curl` to trigger a workflow:
   ```bash
   curl -X POST \
     -H "Authorization: token <your-token>" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
     -d '{"ref":"main"}'
   ```

   Replace:
   - `<your-token>`: Your personal access token.
   - `<owner>`: Your GitHub username or organization name.
   - `<repo>`: The name of your repository.
   - `<workflow_id>`: The workflow filename or ID.
   - `"ref": "main"`: The branch where the workflow should run.

---

### Summary
- **Use `gh` CLI**: Simpler and more user-friendly for triggering workflows remotely.
- **Use cURL with GitHub API**: More flexible for automation and advanced use cases.

---

_**Documentation Maintained By:** Raymond C. Turner_
_**Date:** December 29th, 2025_
