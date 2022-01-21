# Hostname-to-IP-Addresses
Powershell scripti içerisinde yer alan "Get-Content -Path" sonrasında belirtilen .txt dosyası içerisine hostname bilgileri yazılarak .ps1 scripti çalıştırılır. Script çıktısı bir text editörüne kopyalandıktan sonra IP adreslerine match eden Regex ile tüm IP adresleri tespit edilerek kopyalanabilir.

IP Regex: \b(\d{1,3}\.){3}\d{1,3}\b
