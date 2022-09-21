function getIP{
(get-netipaddress).ipv4address | Select-String "192*"
}
write-host(getIP)

$IP = getIP

Write-Host("This machine's IP is $IP.")The main user is (Get-localUser -name "Administrator") The hostname is (hostname) The version of power shell is ($HOST.Version.Major) Todays date is (get-date)