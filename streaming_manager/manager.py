import json
from pathlib import Path
from typing import Dict, List

def load_accounts(path: Path) -> List[Dict]:
    if path.exists():
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_accounts(path: Path, accounts: List[Dict]):
    with path.open('w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=2)

def add_account(path: Path, account: Dict):
    accounts = load_accounts(path)
    accounts.append(account)
    save_accounts(path, accounts)

def remove_account(path: Path, username: str):
    accounts = load_accounts(path)
    accounts = [a for a in accounts if a.get('username') != username]
    save_accounts(path, accounts)

def update_account(path: Path, username: str, updates: Dict):
    accounts = load_accounts(path)
    for acc in accounts:
        if acc.get('username') == username:
            acc.update(updates)
    save_accounts(path, accounts)

def list_accounts(path: Path) -> List[Dict]:
    return load_accounts(path)

def cli():
    import argparse
    parser = argparse.ArgumentParser(description='Manage streaming accounts')
    parser.add_argument('action', choices=['add', 'remove', 'update', 'list'])
    parser.add_argument('--username')
    parser.add_argument('--service')
    parser.add_argument('--plan')
    parser.add_argument('--data', help='Additional data as JSON string')
    parser.add_argument('--storage', default='accounts.json')
    args = parser.parse_args()
    path = Path(args.storage)

    if args.action == 'add':
        if not args.username:
            parser.error('username required for add')
        account = {'username': args.username, 'service': args.service, 'plan': args.plan}
        if args.data:
            account.update(json.loads(args.data))
        add_account(path, account)
    elif args.action == 'remove':
        if not args.username:
            parser.error('username required for remove')
        remove_account(path, args.username)
    elif args.action == 'update':
        if not args.username:
            parser.error('username required for update')
        updates = {}
        if args.service:
            updates['service'] = args.service
        if args.plan:
            updates['plan'] = args.plan
        if args.data:
            updates.update(json.loads(args.data))
        update_account(path, args.username, updates)
    elif args.action == 'list':
        accounts = list_accounts(path)
        print(json.dumps(accounts, indent=2))

if __name__ == '__main__':
    cli()
