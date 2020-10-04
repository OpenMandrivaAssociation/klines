%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		klines
Version:	20.08.1
Release:	2
Epoch:		1
Summary:	Place 5 equal pieces together, but wait, there are 3 new ones
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=klines
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires: 	cmake(ECM)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5Crash)


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
%{_datadir}/qlogging-categories5/klines.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
