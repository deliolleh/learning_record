# JSX

### JS? => JavaScript

### jSX => A syntax extension to JavaScript(JS 확장 문법)

- JavaScript + XML / HTML

- ```jsx
  const element = <h1>Hello, World!</h1>;
  ```



### JSX 역할

- XML/ HTML => JS로 변환 / `React.createElement()` <= JSX들이 다 createElement로 변환됨
- `React.createElement`의  params
  - type: 유형, div/span, react 컴포넌트가 들어갈 수 있음
  - props: 속성들
  - children: 현재 element가 가지고 있는 자식 element
- React에서 JSX 사용이 필수는 아님, 직접 모든 함수를 `createElement`로 작성하면 되기 때문에
- 단, JSX를 사용했을 때 코드가 더 간결해지고 생산성, 가독성이 올라감 사용을 권장



### JSX 장점

- 간결한 코드

  - ```jsx
    <!-- JSX 사용 -->
    <div>Hello, {name}</div>
    ```

  - ```react
    <!-- JSX 사용 X -->
    React.createElement('div', null, `Hello, ${name}`);
    ```

- 가독성 향상 => 버그를 발견하기 쉬움
- Injection Attacks 방어 용이 => 보안성 up
  - Injection Attack: 입력창에 일반적인 문자(숫자, 문자)가 아닌 소스 코드를 직접 입력해 해당 코드가 실행되게 만드는 해킹 방법



### JSX 사용법

- JS 코드 + XML/H