# Odoo Addons Repository

Repository ini berisi kumpulan custom addons Odoo yang dikelola secara terpusat untuk memastikan konsistensi struktur, kualitas kode, dan kemudahan maintenance oleh seluruh tim.


## TUJUAN
- Single source of truth untuk custom addons
- Standar enterprise-grade Odoo module
- Reusable di banyak project Odoo
- Mudah diaudit, direfactor, dan diskalakan
---

## STRUKTUR DIREKTORI

SEMUA MODULE ODOO WAJIB BERADA LANGSUNG DI ROOT PROJECT

Struktur yang BENAR:

```
|-- module_name/
|   |-- __init__.py
|   |-- __manifest__.py
|   |-- models/
|   |-- views/
|   |-- security/
|   |-- data/
|   |-- reports/
|   |-- tests/
|
|-- README.md
|-- .gitignore
```

## DILARANG:
- addons/module_name
- custom_addons/module_name
- nested folder module

---

## ATURAN PENAMAAN MODULE

Format wajib:
<prefix>_<domain>_<feature>

Contoh:
- erp_purchase_request
- erp_account_discount
- hr_attendance_extended

Prefix yang disarankan:
- erp_      : Core ERP
- hr_       : HR
- crm_      : CRM
- stock_    : Inventory
- account_  : Accounting

---

## STANDAR __manifest__.py

Setiap module WAJIB memiliki manifest lengkap.

Field minimum:
- name
- version (18.0.x.x.x)
- category
- summary
- author
- license
- depends
- data
- installable
- application

Aturan manifest:
- Version HARUS mengikuti versi Odoo
- Semua dependency HARUS eksplisit
- Tidak ada business logic di manifest

---

## STRUKTUR INTERNAL MODULE

MODELS
```
models/
- __init__.py
- satu file = satu domain
- hindari god object
- gunakan _inherit secara eksplisit
```

VIEWS
```
views/
- pisahkan menu, form, tree
- xpath harus spesifik dan aman
- hindari xpath global
```

SECURITY
```
security/
- ir.model.access.csv
- security.xml
- semua model WAJIB punya access rule
- jangan hardcode group di Python
```

DATA
```
data/
- sequence.xml
- default_data.xml
- gunakan noupdate untuk data referensi
- tidak boleh ada logic bisnis di XML
```
---

## TESTING (DISARANKAN)

```
tests/
- __init__.py
- test_module.py
```

Fokus test:
- perhitungan (tax, discount, total)
- approval flow
- constraint & validation

---

## CODING STANDARD

- Python mengikuti PEP8
- Business logic di models atau service layer
- Method kecil, fokus, dan testable

DILARANG:
- business logic di controller
- SQL mentah tanpa alasan kuat

---

## DEPENDENCY ANTAR MODULE

- Semua dependency HARUS ada di depends
- DILARANG circular dependency
- Module reusable tidak boleh hardcode company, currency, atau config project

---

## PENGGUNAAN REPOSITORY

Repository ini adalah LIBRARY ADDONS, BUKAN project Odoo runnable.

Tambahkan ke addons_path Odoo atau mount sebagai volume Docker.

---

## ATURAN KONTRIBUSI

Sebelum merge:
- Module bisa install dan upgrade tanpa error
- Manifest valid
- Dependency benar
- Tidak memecahkan backward compatibility

---

## CI / CD PIPELINE

Repository ini TERINTEGRASI dengan CI/CD otomatis.

ATURAN BRANCH:
- branch `staging`  → CI/CD STAGING AKAN BERJALAN OTOMATIS
- branch `master`   → CI/CD PRODUCTION AKAN BERJALAN OTOMATIS

PERILAKU PIPELINE:
- Setiap push ke `staging` akan:
  - Menjalankan CI (lint, test, validation manifest)
  - Melakukan deployment ke environment STAGING
- Setiap push ke `master` akan:
  - Menjalankan CI penuh
  - Melakukan deployment ke environment PRODUCTION

ATURAN PENTING:
- DILARANG push langsung ke `master`
- Semua perubahan HARUS melalui `staging`
- Pastikan module install & upgrade LULUS di staging sebelum merge ke master

---

## PRINSIP UTAMA

CONSISTENCY > SPEED  
CLARITY > CLEVERNESS  
MAINTAINABLE > QUICK FIX
