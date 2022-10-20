def create_apk(apk_name, apk_path, apk_version, apk_version_code, apk_package, apk_activity, apk_icon, apk_channel):
    """
    create a apk
    :param apk_name:
    :param apk_path:
    :param apk_version:
    :param apk_version_code:
    :param apk_package:
    :param apk_activity:
    :param apk_icon:
    :param apk_channel:
    :return:
    """
    # create a apk
    apk_path = os.path.join(apk_path, apk_name)
    if os.path.exists(apk_path):
        shutil.rmtree(apk_path)
    os.makedirs(apk_path)

    # copy apk
    apk_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apk", "base.apk")
    apk_dst = os.path.join(apk_path, "base.apk")
    shutil.copyfile(apk_src, apk_dst)

    # copy icon
    icon_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon", apk_icon)
    icon_dst = os.path.join(apk_path, "icon.png")
    shutil.copyfile(icon_src, icon_dst)

    # copy channel
    channel_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "channel", apk_channel)
    channel_dst = os.path.join(apk_path, "channel.txt")
    shutil.copyfile(channel_src, channel_dst)

    # copy keystore
    keystore_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keystore", "keystore.jks")
    keystore_dst = os.path.join(apk_path, "keystore.jks")
    shutil.copyfile(keystore_src, keystore_dst)

    # copy config
    config_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "config.json")
    config_dst = os.path.join(apk_path, "config.json")
    shutil.copyfile(config_src, config_dst)

    # modify config
    with open(config_dst, "r") as f:
        config = json.load(f)
    config["apk_name"] = apk_name
    config["apk_version"] = apk_version
    config["apk_version_code"] = apk_version_code
    config["apk_package"] = apk_package
    config["apk_activity"] = apk_activity
    with open(config_dst, "w") as f:
        json.dump(config, f, indent=4)

    # modify icon
    icon_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon", apk_icon)
    icon_dst = os.path.join(apk_path, "icon.png")
    shutil.copyfile(icon_src, icon_dst)

    # modify channel
    channel_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "channel", apk_channel)
    channel_dst = os.path.join(apk_path, "channel.txt")
    shutil.copyfile(channel_src, channel_dst)

    # modify keystore
    keystore_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keystore", "keystore.jks")
    keystore_dst = os.path.join(apk_path, "keystore.jks")
    shutil.copyfile(keystore_src, keystore_dst)

    # modify config
    config_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "config.json")
    config_dst = os.path.join(apk_path, "config.json")
    shutil.copyfile(config_src, config_dst)

    # modify config
    with open(config_dst, "r") as f:
        config = json.load(f)
    config["apk_name"] = apk_name
    config["apk_version"] = apk_version
    config["apk_version_code"] = apk_version_code
    config["apk_package"] = apk_package
    config["apk_activity"] = apk_activity
    with open(config_dst, "w") as f:
        json.dump(config, f, indent=4)
