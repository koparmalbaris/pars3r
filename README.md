# Hostname-to-IP-Addresses
Powershell scripti içerisinde yer alan "Get-Content -Path" sonrasında belirtilen .txt dosyası içerisine hostname bilgileri yazılarak .ps1 scripti çalıştırılır. 

Script çıktısı bir text editörüne kopyalandıktan sonra IP adreslerine match eden Regex ile tüm IP adresleri kopyalanabilir.

IP Regex: \b(\d{1,3}\.){3}\d{1,3}\b
Hostname Regex: ([A-Z0-9.-]+\.[A-Z]{2,5})

![Usage-1](https://user-images.githubusercontent.com/45037356/150563601-45cb0e29-683b-4e0c-849a-fe31e3abf421.png)
![Usage-2](https://user-images.githubusercontent.com/45037356/150563614-ad7a1a7e-de5c-498b-a0dc-3df864408c32.png)
![Usage-3](https://user-images.githubusercontent.com/45037356/150563673-6652e6db-10bc-4d15-8136-b4bbd8531b97.png)
