from django.db.backends.mysql import base

# 保存原始的版本检查方法
original_check = base.Database.check_database_version_supported

# 覆盖版本检查方法，跳过检查
def patched_check_database_version_supported(self):
    # 不执行版本检查，允许使用MySQL 5.7.44
    pass

# 应用补丁
base.Database.check_database_version_supported = patched_check_database_version_supported

# 重新导出所有原始模块的内容，使Django能够找到所需的组件
for name in dir(base):
    if not name.startswith('_'):
        globals()[name] = getattr(base, name)