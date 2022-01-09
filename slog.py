globals().update({t:(lambda t,c:lambda m:print(f'[\033[{c}m{t.upper()}\033[0m] {m}'))(t,c)for t,c in{'error':31,'debug':32,'warning':33,'info':34}.items()})
