Summary:	luit application
Summary(pl):	Aplikacja luit
Name:		xorg-app-luit
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/luit-%{version}.tar.bz2
# Source0-md5:	fbe44e739590d3d73f711bfc8a0e33fd
Patch0:		xorg-luit-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
luit application.

%description -l pl
Aplikacja luit.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/luit
%{_mandir}/man1/luit.1x*
