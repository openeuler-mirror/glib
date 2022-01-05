Name:           glib
Epoch:          1
Version:        1.2.10
Release:        56
License:        LGPLv2+
Summary:        GLib is the core library that forms the basis for projects
URL:            http://www.gtk.org/
Source:         https://ftp.gtk.org/pub/gtk/v1.2/glib-1.2.10.tar.gz
BuildRequires:  coreutils libtool make

Patch0001:      glib-1.2.10-isowarning.patch
Patch0002:      glib-1.2.10-gcc34.patch
Patch0003:      glib-1.2.10-underquoted.patch
Patch0004:      glib-1.2.10-no_undefined.patch
Patch0005:      glib-1.2.10-multilib.patch
Patch0006:      glib-1.2.10-unused-dep.patch
Patch0007:      glib-1.2.10-autotools.patch
Patch0008:      glib-1.2.10-format.patch
Patch0009:      glib-1.2.10-gcc5.patch

%description
GLib is the low-level core library that forms the basis for projects such
as GTK and GNOME. It provides data structure handling for C, portability
wrappers, and interfaces for such runtime functionality as an event loop,
threads, dynamic loading, and an object system.

%package        devel
Summary:        Glib development files
Requires:       glib = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description    devel
Libraries and header files for glib development.

%package        help
Summary:        Help document for the glib package
Buildarch:      noarch

%description    help
Help document for the glib package.

%prep
%autosetup -n %{name}-%{version} -p1
install -p -m 0644 /usr/lib/rpm/openEuler/config.guess config.guess
install -p -m 0644 /usr/lib/rpm/openEuler/config.sub config.sub
%build
%configure LIBTOOL=%{_bindir}/libtool
%make_build LIBTOOL=%{_bindir}/libtool
%install
%make_install LIBTOOL=%{_bindir}/libtool
chmod -c a+x %{buildroot}%{_libdir}/lib*.so*
%delete_la_and_a
%check
make check LIBTOOL=%{_bindir}/libtool
%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/glib-config
%{_libdir}/lib*.so
%{_libdir}/glib/
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/aclocal/*

%files help
%{_mandir}/man1/*
%exclude %{_infodir}

%changelog
* Wed Jan 05 2022 xu_ping <xuping33@huawei.com> - 1:1.2.10-56
- fix config.guess and config.sub path error

* Wed Nov 27 2019 Ling Yang <lingyang2@huawei.com> - 1:1.2.10-54
- Package init
