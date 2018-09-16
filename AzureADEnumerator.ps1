# Simple Script made for BalCCon 2k18
# Built by @TanoyBose

Import-Module AzureAD
Echo 'Prompting for credential.'
$AzureAdCred = Get-Credential
Echo 'Attempting to connect to Azure AD'
Connect-AzureAD -Credential $AzureAdCred
echo "Getting Tenant Details"
Get-AzureADTenantDetail | Export-Csv Get-AzureADTenantDetail.csv
echo "Getting Azure AD domain information"
Get-AzureADDomain | Export-Csv Get-AzureADDomain.csv
echo "Getting Azure AD Directory roles"
Get-AzureADDirectoryRole | Export-Csv Get-AzureADDirectoryRole.csv
#Further Enumeration
#Get-AzureADDirectoryRoleMember -ObjectId ""
echo "Extracting Directory Role"
Get-AzureADDirectoryRole | Select-Object ObjectID | ForEach-Object {$val=$_.psobject.Properties.Value; echo "Extracting directory roles of ObjectID: " $val; Get-AzureADDirectoryRoleMember -ObjectId $val | Out-File Get-AzureADDirectoryRole.txt -Append}
Echo "Extracting all azure ad groups"
Get-AzureADGroup -all 1 | Export-Csv Get-AzureADGroup.csv
echo "Extracting Group Members"
Get-AzureADGroup | Select-Object ObjectID | ForEach-Object {$val=$_.psobject.Properties.Value; echo "Extracting Group members of ObjectID: "$val; Get-AzureADGroupMember -ObjectId $val | Out-File Get-AzureADGroupMember.txt -Append}
echo "Extracting all azure ad users"
Get-AzureADUser -All 1 | Export-Csv Get-AzureADUser.csv
echo "Extracting all azure ad devices"
Get-AzureADDevice -All 1 | Export-Csv Get-AzureADDevice_All.csv
echo "Extracting all azure service principals"
Get-AzureADServicePrincipal -All 1 | Export-Csv Get-AzureADServicePrincipal.csv
