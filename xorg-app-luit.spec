Summary:	luit application - locale and ISO 2022 support for Unicode terminals
Summary(pl.UTF-8):	Aplikacja luit - obsługa lokalizacji i ISO 2022 dla terminali unikodowych
Name:		xorg-app-luit
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/luit-%{version}.tar.bz2
# Source0-md5:	4e45233e310d72dce307709761cf241b
Patch0:		xorg-luit-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
luit is a filter that can be run between an arbitrary application and
a UTF-8 terminal emulator. It will convert application output from the
locale's encoding into UTF-8, and convert terminal input from UTF-8
into the locale's encoding.

%description -l pl.UTF-8
luit to filtr, który można uruchomić między dowolną aplikacją a
emulatorem terminala UTF-8. Konwertuje wyjście z aplikacji z kodowania
lokalizacji do UTF-8 oraz wejście terminala z UTF-8 do kodowania
lokalizacji.

%prep
%setup -q -n luit-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/luit
%{_mandir}/man1/luit.1x*
