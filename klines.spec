Name:		klines
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Place 5 equal pieces together, but wait, there are 3 new ones
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=klines
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KLines is a simple but highly addictive one player game.

The player has to move the colored balls around the game board, gathering them
into the lines of the same color by five. Once the line is complete it is
removed from the board, therefore freeing precious space. In the same time the
new balls keep arriving by three after each move, filling up the game board.

%files
%{_kde_bindir}/klines
%{_kde_applicationsdir}/klines.desktop
%{_kde_appsdir}/klines
%{_kde_docdir}/*/*/klines
%{_kde_iconsdir}/hicolor/*/apps/klines.png
%{_kde_datadir}/config.kcfg/klines.kcfg

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

