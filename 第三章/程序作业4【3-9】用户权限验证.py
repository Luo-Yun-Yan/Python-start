user_role=input('用户角色:')
access_level=(
    'admin'if user_role=='administrator' else
    'edit'if user_role=='[editor,contributor]' else
    'view')
print(f'访问权限:{access_level}')