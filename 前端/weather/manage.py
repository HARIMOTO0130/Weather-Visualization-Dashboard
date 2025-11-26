#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
    
    # 在导入和执行命令之前应用MySQL版本检查补丁
    try:
        # 导入Django的基础模块
        import django
        # 导入数据库后端基础类
        from django.db.backends.base.base import BaseDatabaseWrapper
        # 保存原始方法
        original_check = BaseDatabaseWrapper.check_database_version_supported
        # 覆盖为不执行任何操作的方法
        def patched_check(self):
            # 跳过版本检查，允许使用MySQL 5.7.44
            pass
        # 应用补丁到基类
        BaseDatabaseWrapper.check_database_version_supported = patched_check
        print("Successfully patched MySQL version check")
    except Exception as e:
        print(f"Warning: Failed to patch MySQL version check: {e}")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
