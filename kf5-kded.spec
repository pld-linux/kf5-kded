%define		kdeframever	5.84
%define		qtver		5.14.0
%define		kfname		kded

Summary:	Central daemon of KDE work spaces
Name:		kf5-%{kfname}
Version:	5.84.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	bca8477006e6e1fc9689a5584a4c2875
URL:		http://www.kde.org/
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.5
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kcrash-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-kcrash >= %{version}
Requires:	kf5-kdbusaddons >= %{version}
Requires:	kf5-kservice >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs in
the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kded5
%{_datadir}/dbus-1/interfaces/org.kde.kded5.xml
%{_datadir}/dbus-1/services/org.kde.kded5.service
%{_datadir}/kservicetypes5/kdedmodule.desktop
%{_datadir}/qlogging-categories5/kded.categories
%{_mandir}/man8/kded5.8*
%{_desktopdir}/org.kde.kded5.desktop
%lang(ca) %{_mandir}/ca/man8/kded5.8*
%lang(de) %{_mandir}/de/man8/kded5.8*
%lang(es) %{_mandir}/es/man8/kded5.8*
%lang(it) %{_mandir}/it/man8/kded5.8*
%lang(nl) %{_mandir}/nl/man8/kded5.8*
%lang(pt) %{_mandir}/pt/man8/kded5.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/kded5.8*
%lang(ru) %{_mandir}/ru/man8/kded5.8*
%lang(sv) %{_mandir}/sv/man8/kded5.8*
%lang(uk) %{_mandir}/uk/man8/kded5.8*
%{systemduserunitdir}/plasma-kded.service
%{_datadir}/qlogging-categories5/kded.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KDED
