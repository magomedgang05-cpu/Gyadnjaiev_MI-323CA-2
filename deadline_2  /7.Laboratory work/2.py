def build_user_profile(user_id: int, **kwargs) -> dict:
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile

profile = build_user_profile(101, name="Магомед", status="offline", email="magakrut@gmail.com")
print(profile)