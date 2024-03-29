Summary:	Image merging tool
Summary(pl.UTF-8):	Narzędzie do łączenia obrazów
Name:		xmerge
Version:	0.1.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/xmerge/%{name}-%{version}.tar.gz
# Source0-md5:	ffb929265d041f103b7d629d80ab184b
Patch0:		%{name}-opt.patch
URL:		http://xmerge.sourceforge.net
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmerge is an open source program for merging and correcting rotated,
skewed or generally linearly distorted images, featuring a X GUI.

%description -l pl.UTF-8
xmerge jest narzędziem przeznaczonym do łączenia i korygowania
obróconych, przechylonych i w inny sposób zniekształconych liniowo
obrazów. Posiada interfejs graficzny.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	XCC="%{__cc}" \
	XCXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
