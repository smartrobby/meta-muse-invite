const REFERRAL_CODE = "L2FZL2";

const codeElement = document.getElementById("referral-code");
const copyButton = document.getElementById("copy-code");
const noteElement = document.getElementById("referral-note");

if (REFERRAL_CODE.trim()) {
  codeElement.textContent = REFERRAL_CODE.trim();
  copyButton.disabled = false;
  noteElement.textContent = "초대 보상과 적용 가능 여부는 Muse 공식 화면에서 확인해 주세요.";
  copyButton.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(REFERRAL_CODE.trim());
      copyButton.textContent = "복사됨";
      window.setTimeout(() => { copyButton.textContent = "복사"; }, 2200);
    } catch {
      copyButton.textContent = "복사 실패";
    }
  });
}
