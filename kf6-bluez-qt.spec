%define libname %mklibname KF6BluezQt
%define devname %mklibname KF6BluezQt -d
%define git 20230627

Name: kf6-bluez-qt
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/bluez-qt/-/archive/master/bluez-qt-master.tar.bz2#/bluez-qt-%{git}.tar.bz2
Summary: Qt wrapper for the BlueZ DBus API
URL: https://invent.kde.org/frameworks/bluez-qt
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(EGL)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}
Requires: bluez

%description
Qt wrapper for the BlueZ DBus API

%package -n %{libname}
Summary: Qt wrapper for the BlueZ DBus API
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt wrapper for the BlueZ DBus API

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt wrapper for the BlueZ DBus API

%prep
%autosetup -p1 -n bluez-qt-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt6/qml/org/kde/bluezqt
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/BluezQt
%{_libdir}/cmake/KF6BluezQt
%{_libdir}/pkgconfig/KF6BluezQt.pc
%{_libdir}/qt6/mkspecs/modules/qt_BluezQt.pri
%{_libdir}/qt6/doc/KF6BluezQt.*

%files -n %{libname}
%{_libdir}/libKF6BluezQt.so*
