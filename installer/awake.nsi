; includes
!include "MUI2.nsh"
!include "nsDialogs.nsh"
!include "LogicLib.nsh"
!include "x64.nsh"
!include "FileFunc.nsh"

; defines
!define $PRODUCT_NAME "Awake"
!define $APPVERSION "v0.5.1"
!define $PRODUCT_PUBLISHER "adambonneruk"
!define $ICON_PATH "..\src\assets\awake.ico"
!define $REG_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\Awake"

; compiler options
RequestExecutionLevel admin
SetCompressor /SOLID lzma
Unicode True

; settings
Name "${$PRODUCT_NAME} ${$APPVERSION}"
OutFile "Awake Installer (${$APPVERSION}).exe"
BrandingText "${$PRODUCT_PUBLISHER}"

; gui configuration
!define MUI_ICON ${$ICON_PATH}
!define MUI_UNICON ${$ICON_PATH}
!define MUI_ABORTWARNING ; "are you sure you want to quit?" prompt
!define MUI_WELCOMEFINISHPAGE_BITMAP "assets\wizard.bmp"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP ".\assets\header.bmp"
!define MUI_COMPONENTSPAGE_SMALLDESC ; show small description for each component

; mui2 macros/pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "..\LICENCE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

;installer sections
Section "Base Files" SecBaseFiles

	SectionIn RO ; read-only
	SetOutPath $INSTDIR
	DetailPrint "Cleaning install directory"
	RMDIR /r $INSTDIR\*.* ; clean the installation directory

	; copy files given x86 or x86-64 operating system
	${If} ${RunningX64}
		DetailPrint "64-Bit Mode"
		File /r ..\dist\awake\*.*
	${else}
		DetailPrint "32-Bit Mode"
		File /r ..\dist\awake\*.*
	${EndIf}

	; add uninstaller entry to the add/remove programs control panel
	WriteRegStr HKLM "${$REG_PATH}" "DisplayName" "${$PRODUCT_NAME}"
	WriteRegStr HKLM "${$REG_PATH}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "${$REG_PATH}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "${$REG_PATH}" "DisplayIcon" "$\"$INSTDIR\assets\awake.ico$\""
	WriteRegStr HKLM "${$REG_PATH}" "DisplayVersion" "${$APPVERSION}"
	WriteRegStr HKLM "${$REG_PATH}" "Publisher" "${$PRODUCT_PUBLISHER}" ; Not show in Windows 10
	WriteRegDWORD HKLM "${$REG_PATH}" "EstimatedSize" 26986 ; Calculated size based on v0.5.0
	WriteRegDWORD HKLM "${$REG_PATH}" "NoModify" 1
	WriteRegDWORD HKLM "${$REG_PATH}" "NoRepair" 1

	; create uninstaller
	WriteUninstaller "$INSTDIR\uninstall.exe"

SectionEnd

Section "Start Menu Shortcuts" SecStartMenu

	DetailPrint "Creating Start Menu Shortcuts"
	CreateDirectory "$SMPROGRAMS\Awake"
	CreateShortcut "$SMPROGRAMS\Awake\${$PRODUCT_NAME}.lnk" "$INSTDIR\Awake.exe"
	CreateShortcut "$SMPROGRAMS\Awake\Uninstall.lnk" "$INSTDIR\uninstall.exe"

SectionEnd

Section "Desktop Shortcut" SecDeskShort

	DetailPrint "Creating Desktop Shortcut"
	CreateShortcut "$DESKTOP\${$PRODUCT_NAME}.lnk" "$INSTDIR\Awake.exe" "" "$INSTDIR\assets\awake.ico" 0

SectionEnd

Function .onInit

	; set install folder given x86 or x86-64 operating system
	${If} ${RunningX64}
		StrCpy $INSTDIR "$PROGRAMFILES64\Awake"
		SetRegView 64
	${else}
		StrCpy $INSTDIR "$PROGRAMFILES\Awake"
		SetRegView 32
	${EndIf}

FunctionEnd

; component descriptions
LangString DESC_SecBaseFiles ${LANG_ENGLISH} 	"Install the Awake program and all dependencies"
LangString DESC_SecStartMenu ${LANG_ENGLISH} 	"Install Windows Start Menu shortcuts"
LangString DESC_SecDeskShort ${LANG_ENGLISH} 	"Install Windows desktop shortcut"

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecBaseFiles} $(DESC_SecBaseFiles)
    !insertmacro MUI_DESCRIPTION_TEXT ${SecStartMenu} $(DESC_SecStartMenu)
    !insertmacro MUI_DESCRIPTION_TEXT ${SecDeskShort} $(DESC_SecDeskShort)
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; configure uninstaller
Section "Uninstall"

	RMDIR /r $INSTDIR\*.* ; clean the installation directory
	Delete "$DESKTOP\${$PRODUCT_NAME}.lnk" ; delete desktop shortcut

	; remove start menu shortcuts
	Delete "$SMPROGRAMS\Awake\*.lnk"
	RMDir "$SMPROGRAMS\Awake"

	; set registry view given x86 or x86-64 operating system
	${If} ${RunningX64}
		SetRegView 64
	${else}
		SetRegView 32
	${EndIf}

	DeleteRegKey HKLM "${$REG_PATH}" ; delete windows add/remove programs key

SectionEnd
