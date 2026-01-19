# Comprehensive QA Test Suite - E-Commerce Platform 🚀

[![CI/CD](https://github.com/okurenes/qa-comprehensive-test-suite/actions/workflows/test.yml/badge.svg)](https://github.com/okurenes/qa-comprehensive-test-suite/actions)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Kapsamlı QA test otomasyon suite'i. UI, API, Database ve Performance testlerini içerir.

**Geliştirici:** Enes Okur  
**LinkedIn:** [linkedin.com/in/enes-okur-133871136](https://www.linkedin.com/in/enes-okur-133871136)  
**Email:** okurenes.official@gmail.com

---

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Test Kapsamı](#test-kapsamı)
- [CI/CD](#cicd)
- [Dokümantasyon](#dokümantasyon)
- [Raporlama](#raporlama)

---

## 🎯 Özellikler

### ✅ UI Test Automation
- **Framework:** Selenium WebDriver + Python
- **Design Pattern:** Page Object Model (POM)
- **Test Runner:** Pytest
- **Kapsam:** 33 UI test senaryosu
- **Marker:** `@pytest.mark.ui`

### ✅ API Test Automation
- **Framework:** Requests + Python
- **Validasyon:** Response validator, Schema validation
- **Kapsam:** 20 API test senaryosu
- **Marker:** `@pytest.mark.api`

### ✅ Database Testing
- **Database:** PostgreSQL
- **Kapsam:** Data integrity, Query performance
- **Test Count:** 6 test senaryosu
- **Marker:** `@pytest.mark.db`

### ✅ Performance Testing
- **Tool:** Locust
- **Test Tipleri:** Load testing, Stress testing
- **Metrikler:** Response time, Throughput, Error rate

### ✅ CI/CD Integration
- **Platform:** GitHub Actions
- **Trigger:** Push, PR, Scheduled (daily)
- **Reports:** HTML test reports as artifacts

---

## 📁 Proje Yapısı
cat > README.md << 'EOF'
# Comprehensive QA Test Suite - E-Commerce Platform 🚀

[![CI/CD](https://github.com/okurenes/qa-comprehensive-test-suite/actions/workflows/test.yml/badge.svg)](https://github.com/okurenes/qa-comprehensive-test-suite/actions)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Kapsamlı QA test otomasyon suite'i. UI, API, Database ve Performance testlerini içerir.

**Geliştirici:** Enes Okur  
**LinkedIn:** [linkedin.com/in/enes-okur-133871136](https://www.linkedin.com/in/enes-okur-133871136)  
**Email:** okurenes.official@gmail.com

---

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Test Kapsamı](#test-kapsamı)
- [CI/CD](#cicd)
- [Dokümantasyon](#dokümantasyon)
- [Raporlama](#raporlama)

---

## 🎯 Özellikler

### ✅ UI Test Automation
- **Framework:** Selenium WebDriver + Python
- **Design Pattern:** Page Object Model (POM)
- **Test Runner:** Pytest
- **Kapsam:** 33 UI test senaryosu
- **Marker:** `@pytest.mark.ui`

### ✅ API Test Automation
- **Framework:** Requests + Python
- **Validasyon:** Response validator, Schema validation
- **Kapsam:** 20 API test senaryosu
- **Marker:** `@pytest.mark.api`

### ✅ Database Testing
- **Database:** PostgreSQL
- **Kapsam:** Data integrity, Query performance
- **Test Count:** 6 test senaryosu
- **Marker:** `@pytest.mark.db`

### ✅ Performance Testing
- **Tool:** Locust
- **Test Tipleri:** Load testing, Stress testing
- **Metrikler:** Response time, Throughput, Error rate

### ✅ CI/CD Integration
- **Platform:** GitHub Actions
- **Trigger:** Push, PR, Scheduled (daily)
- **Reports:** HTML test reports as artifacts

---

## 📁 Proje Yapısı
```
qa-comprehensive-test-suite/
├── ui_tests/                   # UI Test Automation
│   ├── pages/                  # Page Object Models
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/                  # UI Test Cases
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   └── utils/                  # UI Utilities
│       └── test_data.py
│
├── api_tests/                  # API Test Automation
│   ├── tests/                  # API Test Cases
│   │   ├── test_users_api.py
│   │   ├── test_auth_api.py
│   │   └── test_schema_validation.py
│   └── utils/                  # API Utilities
│       ├── api_client.py
│       └── response_validator.py
│
├── db_tests/                   # Database Testing
│   ├── tests/                  # DB Test Cases
│   │   └── test_database.py
│   └── utils/                  # DB Utilities
│       └── db_connection.py
│
├── performance_tests/          # Performance Testing
│   └── locustfile.py          # Locust scenarios
│
├── documentation/              # Test Documentation
│   ├── test_strategy.md
│   ├── test_plan.md
│   └── bug_report_template.md
│
├── .github/workflows/          # CI/CD
│   └── test.yml               # GitHub Actions
│
├── reports/                    # Test Reports
├── test_data/                  # Test Data Files
├── config.py                   # Configuration
├── conftest.py                # Pytest fixtures
├── pytest.ini                  # Pytest config
├── requirements.txt            # Dependencies
├── .env.example               # Environment variables template
└── README.md                   # This file
```

---

## 🛠️ Kurulum

### 1. Repository'yi Klonla
```bash
git clone https://github.com/okurenes/qa-comprehensive-test-suite.git
cd qa-comprehensive-test-suite
```

### 2. Virtual Environment Oluştur
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Dependencies Yükle
```bash
pip install -r requirements.txt
```

### 4. Environment Variables Ayarla
```bash
cp .env.example .env
# .env dosyasını düzenle
```

---

## ▶️ Kullanım

### UI Testleri Çalıştır
```bash
# Tüm UI testleri
pytest ui_tests/ -v

# Sadece smoke testleri
pytest -m "ui and smoke" -v

# Sadece critical testleri
pytest -m "ui and critical" -v

# Belirli bir test dosyası
pytest ui_tests/tests/test_login.py -v
```

### API Testleri Çalıştır
```bash
# Tüm API testleri
pytest api_tests/ -v

# Sadece API smoke testleri
pytest -m "api and smoke" -v
```

### Database Testleri Çalıştır
```bash
pytest db_tests/ -v -m db
```

### Tüm Testleri Çalıştır
```bash
pytest -v
```

### Performance Testi Çalıştır
```bash
# Web UI load test
locust -f performance_tests/locustfile.py --host=https://www.saucedemo.com --users 10 --spawn-rate 2

# API load test
locust -f performance_tests/locustfile.py --host=https://reqres.in/api --users 50 --spawn-rate 5
```

---

## 🧪 Test Kapsamı

### Test Senaryoları Özeti

| Test Suite | Test Sayısı | Marker | Priority |
|------------|------------|--------|----------|
| Login Tests | 7 | `ui` | Critical |
| Products Tests | 9 | `ui` | High |
| Cart Tests | 8 | `ui` | High |
| Checkout Tests | 9 | `ui` | Critical |
| API Users Tests | 9 | `api` | High |
| API Auth Tests | 7 | `api` | Critical |
| Schema Validation | 4 | `api` | Medium |
| Database Tests | 6 | `db` | Medium |
| **TOPLAM** | **59** | - | - |

### Test Tipleri

- ✅ **Smoke Tests:** Kritik fonksiyonları hızlıca doğrular
- ✅ **Regression Tests:** Tüm fonksiyonları kapsamlı test eder
- ✅ **Integration Tests:** Sistemler arası entegrasyonları test eder
- ✅ **Performance Tests:** Load ve stress testleri

---

## 🔄 CI/CD

### GitHub Actions Workflow

Otomatik test çalıştırma:

- ✅ Her `push` ve `pull request`'te
- ✅ Günlük scheduled run (09:00 UTC)
- ✅ Test raporları artifact olarak saklanır

### Workflow Jobs

1. **UI Tests:** Smoke ve critical UI testleri
2. **API Tests:** Tüm API testleri
3. **Regression Tests:** Nightly full regression
4. **Test Summary:** Özet rapor

---

## 📊 Raporlama

### HTML Reports

Testler çalıştıktan sonra `reports/` klasöründe HTML raporları oluşturulur:
```bash
# Raporları görüntüle
open reports/report.html  # Mac
start reports/report.html # Windows
```

### CI/CD Reports

GitHub Actions'da testler tamamlandıktan sonra **Artifacts** bölümünden raporları indirebilirsiniz.

---

## 📚 Dokümantasyon

- [Test Strategy](documentation/test_strategy.md)
- [Test Plan](documentation/test_plan.md)
- [Bug Report Template](documentation/bug_report_template.md)

---

## 🔧 Teknolojiler

| Kategori | Teknoloji |
|----------|-----------|
| **Language** | Python 3.10+ |
| **UI Automation** | Selenium WebDriver 4.16 |
| **API Testing** | Requests, JSONSchema |
| **Database** | PostgreSQL, psycopg2 |
| **Performance** | Locust |
| **Test Framework** | Pytest |
| **Reporting** | pytest-html, Allure |
| **CI/CD** | GitHub Actions |
| **Version Control** | Git |

---

## 💡 Best Practices

✅ **Page Object Model** kullanımı  
✅ **Reusable components** ve utilities  
✅ **Clear test naming** conventions  
✅ **Comprehensive logging**  
✅ **Environment based configuration**  
✅ **Proper error handling**  
✅ **Test data separation**  
✅ **CI/CD integration**  

---

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır!

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

---

## 📧 İletişim

**Enes Okur**  
📧 Email: okurenes.official@gmail.com  
💼 LinkedIn: [enes-okur-133871136](https://www.linkedin.com/in/enes-okur-133871136)  
🐙 GitHub: [okurenes](https://github.com/okurenes)

---

## 📝 Lisans

Bu proje MIT lisansı altındadır.

---

## ⭐ Yıldız Vermeyi Unutmayın!

Eğer bu proje işinize yaradıysa, lütfen bir ⭐ verin!
