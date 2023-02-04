https://python-poetry.org/docs/

위 페이지에서 

```curl -sSL https://install.python-poetry.org | python3 -```

위 명령어를 통해 poetry를 깔았지만 

```poetry```

```zsh: command not found: poetry```

찾을 수가 없다고 뜬다ㅠㅠ



다행히 아래 댓글을 보니 누가 문제를 해결해 올려 주셨다. 

```
zsh 환경에서 ‘ zsh: command not found: poetry ’ 해결법


1. 일단 재설치를 해봅니다.

재설치했을 때, 이미 설치되었다고 뜬다면

2번으로 진행하세요.

2. 홈 디렉토리 (~) 가셔서 .local / bin 에 poetry 파일이 있는지 확인하세요.

3. 홈 디렉토리의 .zshrc 파일에 다음 줄을 추가해주세요.

export PATH=$HOME/.local/bin:$PATH

만약 2번에서 다른 경로에 poetry 바이너리 파일이 설치되었다면,

export PATH=:$PATH

를 적어주시면 됩니다.

4. 터미널을 재시작하시고 poetry를 입력해보세요.
```

그런데 ls 를 쳐 봐도 `.local/bin`가 안 보인다. 

알고보니 숨긴 처리 되어 있다고 한다. 그냥 무지성으로 쳐 보면 나온다. 

다행히 poetry는 있었다. 

다시 홈으로 돌아와서 ```.zshrc``` 이렇게 하면 안뜬다.

```vim ~/.zshrc``` 이렇게 쳐야 한다. 

이렇게 하면 어떤 새로운 화면이 나오는데. 거기에 ```export PATH=$HOME/.local/bin:$PATH```을 추가 해 주었다. 

참고로 거기를 나오는 방법는 ```:wq```이다. 

그리고 다시 poetry를 쳐 보니 잘 나온다!!!



참고한 블로그

https://zionh.tistory.com/28

https://triplexlab.tistory.com/110
