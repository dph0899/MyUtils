# ImageMagick Configuration
/etc/ImageMagick-6/policy.xml:
```
<policy domain="coder" rights="read | write" pattern="PDF" />
<policy domain="resource" name="disk" value="250GiB"/>
<policy domain="resource" name="file" value="3000"/>
<policy domain="resource" name="width" value="16KP"/>
<policy domain="resource" name="height" value="16KP"/>
```

bash
```
export MAGICK_TEMPORARY_PATH = some_dir
echo fs.file-max = 3000 >> /etc/sysctl.conf
```

Modify this line in /etc/systemd/system.conf
```
#DefaultLimitNOFILE=8192:524288
```