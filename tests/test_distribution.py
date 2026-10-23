"""Exercise the actual allowlist packager, not a mocked manifest."""
from pathlib import Path
import json,shutil,subprocess,unittest
ROOT=Path(__file__).resolve().parents[1]
class FeedbackDistribution(unittest.TestCase):
    def test_feedback_runtime_is_in_the_packaged_distribution(self):
        node=shutil.which('node');assert node is not None,'Node.js is required for distribution tests'
        result=subprocess.run([node,'scripts/package-dist.cjs'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',check=True)
        manifest=json.loads(result.stdout);paths={item['path'] for item in manifest['files']}
        self.assertIn('js/validation.js',paths,'Feedback validation must be present in the actual distribution')
        self.assertEqual((ROOT/'js/validation.js').read_bytes(),(ROOT/'dist/js/validation.js').read_bytes())
        self.assertIn('./js/validation.js',(ROOT/'dist/index.html').read_text(encoding='utf-8'))
if __name__=='__main__':unittest.main()
