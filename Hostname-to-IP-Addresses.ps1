[string[]] $hostnames = Get-Content -Path C:\Users\Desktop\hostnames.txt

$ips = ""
foreach ($myhost in $hosts)
{
    try
    {
        $ipaddress = [System.Net.Dns]::GetHostAddresses($myhost)
        write-host "SOLVED " + $myhost + " to -> " + $ipaddress
        if ([string]::IsNullOrEmpty($ips))
        {

            $ips = $ipaddress
            continue;
        }
        $ips = $ips + "," + $ipaddress
    }

    catch
    {
        write-host $_
    }
}
write-host $ips