# Oryo Browser

DÉy lÖ d? †n trçnh duy?t ma ngu?n m? Oryo du?c ph†t tri?n vÖ t?i uu b?i Sakayori Studio. 

LUU Y QUAN TR?NG: Repository nÖy KHONG ph?i lÖ toÖn b? ma ngu?n (Full Source) c?a trçnh duy?t. DÉy ch? lÖ noi luu tr? c†c file c?u hçnh thuong hi?u (Rebrand), c†c b?n v† l?i vÖ ma ngu?n C++ tóy bi?n nÉng cao nh?m t?i uu h¢a hi?u nang vÖ gi?m lu?ng RAM tiàu th? c?c h?n so v?i Chromium g?c.

## Yàu c?u h? th?ng (Requirements) d? build d? †n
* H? di?u hÖnh: Windows 10/11 64-bit (da b?t Developer Mode).
* ? c?ng: Tr?ng t?i thi?u 100 GB (khuy?n kh°ch dóng ? SSD t?c d? cao).
* Cìng c? b?t bu?c: B? cìng c? depot_tools c?a Google vÖ Microsoft Visual Studio (d?y d? g¢i C++ vÖ Windows SDK tuong th°ch v?i Chromium).

## Hu?ng d?n cÖi d?t vÖ d?ng b? dÖnh cho Contributor
D? c¢ d?y d? b? ngu?n vÖ b?t d?u l?p trçnh, b?n c?n th?c hi?n theo c†c bu?c sau:

1. T?i toÖn b? ma ngu?n Chromium g?c c?a Google (kho?ng 30-40 GB) v? m†y thìng qua cìng c? fetch c?a depot_tools:
   fetch chromium

2. Di chuy?n vÖo thu m?c ngu?n v?a t?i:
   cd src

3. Kh?i t?o k?t n?i Git t?i repository Oryo nÖy:
   git init
   git remote add origin https://github.com/Sakayorii/Oryo-Browser.git

4. Ti?n hÖnh kÇo ma ngu?n tóy bi?n c?a Oryo v? d? ghi dä t? d?ng vÖo c?u tr£c thu m?c g?c:
   git pull origin main --allow-unrelated-histories

5. D?ng b? l?i c†c thu vi?n bàn th? ba c?a Google:
   gclient sync

## L?nh t?o file c?u hçnh vÖ Build trçnh duy?t
Sau khi d?ng b? xong, b?n ch?y c†c l?nh sau b?ng CMD/PowerShell v?i quy?n Administrator d? ti?n hÖnh biàn d?ch:

1. N?p l?i so d? build graph d? h? th?ng nh?n di?n target m?i:
   gn gen out\Default

2. Ti?n hÖnh build phiàn b?n Oryo d?c b?n b?ng Ninja:
   autoninja -C out\Default oryo
