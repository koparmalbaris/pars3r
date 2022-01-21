[string[]] $hosts = Get-Content -Path Z:\Hostnames.txt

$ips = ""
foreach ($myhost in $hosts)
{
    try
    {
        $ipaddress = [System.Net.Dns]::GetHostAddresses($myhost)
        write-host "s0lv3d:" $myhost" to -->" $ipaddress
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
write-host
write-host "One-line All IP addresses:" $ips
write-host
