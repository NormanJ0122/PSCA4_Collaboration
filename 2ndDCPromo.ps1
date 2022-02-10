Install-ADDSDomainController -NoGlobalCatalog:$false -CreateDnsDelegation:$false -Credential (Get-Credential) -CriticalReplicationOnly:$false -DatabasePath "C:\Windows\NTDS" -DomainName "HUNT.com" -InstallDns:$true -LogPath "C:\Windows\NTDS" -NoRebootOnCompletion:$false -ReplicationSourceDC "NOR-DC1.HUNT.com" -SiteName "Norway" -SysvolPath "C:\Windows\SYSVOL" -Force:$true

