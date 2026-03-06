#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		klines
Version:	25.12.3
Release:	%{?git:0.%{git}.}1
Summary:	Place 6 equal pieces together, but wait, there are 3 new ones
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=klines
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/klines/-/archive/%{gitbranch}/klines-%{gitbranchd}.tar.bz2#/klines-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/klines-%{version}.tar.xz
%endif
BuildRequires: 	cmake(ECM)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6Crash)

%rename plasma6-klines

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KLines is a simple but highly addictive one player game.

The player has to move the colored balls around the game board, gathering them
into the lines of the same color by five. Once the line is complete it is
removed from the board, therefore freeing precious space. In the same time the
new balls keep arriving by three after each move, filling up the game board.

%files -f %{name}.lang
%{_bindir}/klines
%{_datadir}/applications/org.kde.klines.desktop
%{_iconsdir}/hicolor/*/apps/klines.png
%{_datadir}/config.kcfg/klines.kcfg
%{_datadir}/klines/themes/*
%{_datadir}/metainfo/org.kde.klines.appdata.xml
%{_datadir}/qlogging-categories6/klines.categories
%{_datadir}/qlogging-categories6/klines.renamecategories
