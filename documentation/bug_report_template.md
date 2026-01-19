# Bug Report Template

## Bug ID: [BUG-XXX]

### Summary
[Kısa ve açık bug özeti]

### Environment
- **OS:** macOS 14.0
- **Browser:** Chrome 120.0
- **Application Version:** 1.0.0
- **Test Environment:** Staging

### Priority
- [ ] Critical
- [ ] High
- [ ] Medium
- [ ] Low

### Severity
- [ ] Blocker
- [ ] Major
- [ ] Minor
- [ ] Trivial

### Steps to Reproduce
1. [Adım 1]
2. [Adım 2]
3. [Adım 3]

### Expected Result
[Beklenen davranış]

### Actual Result
[Gerçekleşen davranış]

### Screenshots/Videos
[Screenshot veya video URL'si]

### Additional Information
- **Console Errors:** [Varsa console hataları]
- **Network Errors:** [Varsa network hataları]
- **Reproducibility:** Always / Sometimes / Rare

### Test Data Used
- **Username:** standard_user
- **Test Case ID:** TC-XXX

### Suggested Fix
[Opsiyonel - Önerilen çözüm]

---

## Example Bug Report

## Bug ID: BUG-001

### Summary
Login sayfasında "Locked User" ile giriş yapıldığında hata mesajı görüntülenmiyor

### Environment
- **OS:** macOS 14.0
- **Browser:** Chrome 120.0.6099.129
- **Application Version:** 1.0.0
- **Test Environment:** Staging

### Priority
- [x] High
- [ ] Medium
- [ ] Low

### Severity
- [ ] Blocker
- [x] Major
- [ ] Minor

### Steps to Reproduce
1. https://www.saucedemo.com sayfasını aç
2. Username: "locked_out_user" gir
3. Password: "secret_sauce" gir
4. Login butonuna tıkla

### Expected Result
"Epic sadface: Sorry, this user has been locked out" hata mesajı görüntülenmeli

### Actual Result
Hata mesajı görüntülenmedi, sayfa yeniden yüklendi

### Screenshots/Videos
![Screenshot](link-to-screenshot)

### Additional Information
- **Console Errors:** Yok
- **Network Errors:** 403 Forbidden
- **Reproducibility:** Always

### Test Data Used
- **Username:** locked_out_user
- **Password:** secret_sauce
- **Test Case ID:** TC-004

### Suggested Fix
Frontend'de error response handling kontrolü yapılmalı
