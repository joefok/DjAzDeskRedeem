$env:HostIP = (
    Get-NetIPConfiguration |
    Where-Object {
        $_.IPv4DefaultGateway -ne $null -and
        $_.NetAdapter.Status -ne "Disconnected"
    }
).IPv4Address.IPAddress
$prefix = $env:HostIP.Split(".")
$ip_target = $env:HostIP
$ip_target = [string]$ip_target.trim()

$mac = (Get-WmiObject win32_networkadapterconfiguration | Where-Object {$_.IPAddress -match $ip_target}).macaddress
$mac = $mac.Trim()
$url = 'http://127.0.0.1:8000/?token={0}'-f $mac

start-process $url