Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

Rename-Computer TPA-DC2

New-NetIPAddress -IPAddress 192.168.0.230 -PrefixLength 24 -DefaultGateway 192.168.0.254 -InterfaceAlias "Ethernet"

Set-DnsClientServerAddress 192.168.0.229

Add-Computer -DomainName Hunt.com -Credential "Hunt\Justin Norman"

Restart-Computer