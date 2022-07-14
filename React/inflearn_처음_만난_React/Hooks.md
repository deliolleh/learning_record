# Hooks

## Component

- Function Component & Class Component
- Component 안의 state: 렌더링에 관한 데이터 관리
- 함수 컴포넌트
  - state 사용 불가
  - Lifecycle에 따른 기능 구현 불가
- 클래스 컴포넌트
  - 생성자에서 state 정의
  - `setState()`함수를 통해 state 업데이트
  - Lifecycle methods 제공
- 함수 컴포넌트에 state와 Lifecycle 역할을 할 수 있는 `Hooks` => Class Component의 기능을 사용할 수 있음



## Hook

- 갈고리 => 원래 존재하는 어떤 기능에 끼어들어가 같이 수행되는 것(유사한 형태로 Web Hook)
- Hook은 `use`라는 단어로 시작함 - 각 기능을 사용하겠다는 의미

###  `useState()`

- state를 사용하기 위한 Hook
- 함수 컴포넌트에서는 기본적으로 state를 제공하지 않기 때문에 사용

- 사용법

  - ```react
    const [변수명, set함수명] = useState(초기값);
    ```

- ```react
  import React, { useState } from "react";
  
  function Counter(props) {
  	const [count, setCount] = useState(0);
      <!--
  	클래스 컴포넌트에서는 setState 하나로 모든 state 값을 업데이트 할 수 있지만
  	useState에서는 변수 각각에 대해 set함수가 따로 존재함
   	-->
      
      return (
      	<div>
          	<p>총 {count}번 클릭했습니다.</p>
              <button onClick={() => setCount(count + 1)}>
                  클릭
              </button>
          </div>
      )
  }
  ```



### `useEffect()`

- Side effect를 수행하기 위한 Hook

- Side effect? => 부작용, 개발자가 의도하지 않은 버그(일반적, 일반 개발)

  - 효과, 영향(in React) / 서버에서 데이터를 받아오거나 수동으로 DOM을 변경하는 과정
  - 다른 컴포넌트에 영향을 끼칠 수 있고, 렌더링 중에는 작업이 완료될 수 없기 때문에 => 렌더링이 끝난 이후에 실행해야하는 작업들 => 그래서 사이드로 실행되어서 *Side Effect*

- Class Component의 생명주기 함수인 `ComponentDidMount, ComponentDidUpdate, ComponentWillUnmount`와 동일한 기능을 하나로 통합해서 제공

- 사용법

  - ```react
    useEffect(이펙트 함수, 의존성 배열);
    <!--
    	의존성 배열: 이 이팩트가 의존하고 있는 배열
    	배열 안의 값이 하나라도 바뀐다면 Effect함수가 실행됨
    	기본적으로 Effect 함수는 처음 컴포넌트가 렌더링된 이후와
    	업데이트로 인한 재 렌더링 이후에 실행
    -->
    
    <!-- 만약 Effect function이 mount, unmount시에 단 한 번씩만 실행하고 싶다면 -->
    useEffect(이펙트 함수, []);
    <!--
    	이렇게하면 이펙트가 props나 state에 있는 어떤 값이라도 의존하지 않으므로
    	여러번 실행되지 않음
    -->
    
    useEffect(이펙트함수);
    <!--
    	의존성 배열을 생략하면 컴포넌트가 업데이트 될 때마다 호출됨
    -->
    ```

- 예시

  ```react
  import React, { useState, useEffect } from "react";
  
  function Counter(props) {
      const [count, setCount] = useState(0);
      
      // componentDidMount, componentDidupdate와 비슷하게 작동
      useEffect(() => {
          // 브라우저 API를 사용해서 document의 title을 업데이트
          document.title = `You clicked ${count}  times`;
      });
      
      return (
      	<div>
          	<p>총 {count}번 클릭했습니다.</p>
              <button onClick={() => setCount(count + 1)}>
              	클릭
              </button>
          </div>
      );
  }
  ```

  ```react
  import React, { useState, useEffect } from "react";
  
  function UserStatus(props) {
      const[isOnline, setIsOnline] = useState(null);
      
      function handleStatusChange(status) {
          setIsOnline(status.isONline);
      }
      
      useEffect(() => {
          ServerAPI.subscribeUserStatus(props.user.id, handleStatusChange);
          return () => {
              ServerAPI.unsubscribeUserStatus(props.user.id, handleStatusChange);
  		};
          <!--
  			컴포넌트가 unmount 될 때 호출됨
  		-->
      });
      
      if (isOnline == null) {
              return '대기 중...';
      }
      return isOnline? '온라인' : '오프라인';
  }
  ```

  ```react
  userEffect(() => {
      // 컴포넌트가 마운트가 된 이후,
      // 의존성 배열에 있는 변수들 중 하나라도 값이 변경되었을 때 실행 됨
      // 의존성 배열에 빈 배열을 넣으면 마운트와 언마운트시에 단 한 번씩만 실행됨
      // 의존성 배열 생략 시 컴포넌트 업데이트 시마다 실행됨
      ...
      
      return () => {
          // 컴포넌트가 마운트 해제되기 전에 실행됨
          ...
      }
      
  }, [의존성 변수1, 의존성 변수2, ....]);
  ```

- `useEffect` Hook은 하나의 컴포넌트에 여러 개를 사용할 수 있다



### `useMemo()`

- *Memoized value를 리턴하는* Hook

- Memoized value? => useMemo와 useCallback에서 중요

- Memoization: (컴퓨터 분야에서) 최적화를 위해 사용하는 개념, 비용(연산량)이 높은 함수의 호출 결과를 저장해두었다가 같은 입력값으로 함수가 호출되면 새로 함수를 호출하지 않고 이전에 저장해둔 결과를 바로 반환하는 것
  - 함수 호출의 결과를 받기까지의 시간이 짧아지고, 불필요한 중복 연산을 하지 않기 때문에 컴퓨터의 자원을 적게 사용함

- Memoized value: memoized된 결과값 => memo

- 예시

  ```react
  const memoizedValue = useMemo(
  	() => {
          return computeExpensiveValue(의존성 변수1, 의존성 변수2);
      },
      // memoized 생성 함수
      [의존성 변수1, 의존성 변수2]
  );
  // 의존성 배열에 들어있는 변수가 변했을 때에만
  // 새로 create 함수를 호출해 결과값을 반환
  // 아닐 떄는 기존 함수의 결과값이 그대로 반환
  ```

- `useMemo`를 사용하면 컴포넌트가 다시 렌더링 될 때마다 연산량이 높은 작업의 반복을 피할 수 있음

- => 빠른 렌더링 속도

- `useMemo`로 전달된 함수는 렌더링이 일어나는 동안 실행된다는 점(☆) => Side effect들이 들어가지 않도록 조심

- 의존성 배열을 넣지 않은 경우, 매 렌더링마다 함수가 실행됨 => `useMemo`사용 의미가 없음

  ```react
  const memoizedValue = useMemo(
  	() => computeExpensiveValue(a, b)
  );
  ```

- 의존성 배열이 빈 배열일 경우, 컴포넌트 마운트 시에만 호출 됨 => 마운트 이후에는 값이 변경되지 않음



### `useCallback()`

- `useMemo`와 유사하지만 값이 아닌 함수를 반환(함수를 새로 정의해서 리턴)

- `useMemo`처럼 함수(Callback)와 의존성 배열를 parms로 가진다

- 의존성 배열에 있는 변수 중 하나라도 변경되면 Memoization된 Callback 함수를 반환

- 의존성 배열에 따라 Memoized된 값을 반환 => `useMemo()` Hook과 동일

- 즉 `useMemo`와 `useCallback`은 동일한 역할을 수행

  ```react
  useCallback(함수, 의존성 배열);
  
  useMemo(() => 함수, 의존성 배열);
  ```

- `useCallback` hook을 사용하지 않고 컴포넌트 내의 함수를 정의한다면, 매번 렌더링이 일어날 때마다 함수가 새로 정의됨 => `useCallback`을 사용해 특정 변수의 값이 변한 경우에만 함수를 다시 정의하도록 해 불필요한 반복 작업을 제거



### `useRef()`: Reference를 사용하기 위한 Hook

- Reference? - 특정 컴포넌트에 접근할 수 있는 객체 => `useRef()`는 이런 Reference 객체를 반환

- refObject(Ref 객체)의 current 속성: 현재 참고하고 있는 Element

- 사용법

  ```react
  const refContainer = useRef(초기값);
  // 해당 초기값으로 초기화된 Ref 객체를 반환
  // 초기값이 null이라면 currnet=null인 객체 반환
  ```

- 반환된 객체는 Component의 Lifetime 전체에 걸쳐 유지 => 컴포넌트가 Unmount될 때까지 유지

- 변경가능한 current 속성을 가진 하나의 상자

- 내부의 데이터가 변경되었을 때 별도로 알리지 않음(재 렌더링 없음)

- DOM 노드의 변화를 알기 위해서는 Callback ref를 사용해야함 => ref가 다른 노드에 연결될 때마다 callback을 호출함



## Hook의 규칙

### Hook은 무조건 최상위 레벨에서만 작성되어야 한다

- 최상위 레벨? => React 함수 컴포넌트의 최상위 레벨
- 반복문, 조건문, 중첩된 함수 안에서 Hook을 호출하면 안된다
- **Hook은 컴포넌트가 렌더링될 때마다 매번 같은 순서로 호출되어야 한다**
- 그래야 React가 다수의 useState Hook과 useEffect Hook의 호출에서 컴포넌트의 State를 올바르게 관리할 수 있음



### React 함수 컴포넌트에서만 Hook을 호출해야 한다

- 일반적인 J.S 함수에서 Hook을 호출하면 안된다
- Hook은 React 함수 컴포넌트에서 호출하거나 직접 만든 Custom Hook에서만 호출할 수 있음
- React 컴포넌트의 State와 관련된 로직은 SourceCode를 통해 명확하게 확인이 가능해야 함



### ※ `eslint-plugin-react-hooks`

- Hook의 규칙과 관련되어 개발에 도움이 되는 패키지
- hook의 규칙을 따르도록 강제하는 plugin
- eslint: j.s 코드에 발견되는 문제 패턴을 식별하기 위한 정적 코드 분석 도구
- react 컴포넌트가 hook의 규칙을 따르는지 아닌지를 판별할 수 있게 도와줌
- 의존성 배열이 잘못된 경우 경고 표시를 해주며, 고칠 방법을 제안함
- https://www.npmjs.com/package/eslint-plugin-react-hooks



## Custom Hook 만들기

- 여러 컴포넌트에서 반복적으로 사용되는 로직을 Hook으로 만들어 재사용하기 위함

- Custom Hook을 만들어야 하는 상황 - 중복되는 코드를 추출해 Custom Hook으로 만듦
- 여러 개의 javaScript 함수에서 하나의 로직을 공유하도록 함
- **이름이 use로 시작하고 내부에서 다른 hook을 호출하는 하나의 javaScript 함수**



### Custom Hook 추출

```react
import { useState, useEffect } from "react";

function useUserStatus(usedId) {
    // 목적: user의 on/offline 상태를 구독하는 것
    const [isOnline, setIsOnline] = useState(null);
    
    useFfect(() => {
        function handleStatusChange(status) {
            setIsONline(status.isOnline);
        }
        
        ServerAPI.subscribeUserStatus(userId, handleStatusChange);
        return () => {
            ServerAPI.unsubscribeUserStatus(userId, handleStatusChange);
        };
    });
    
    return isOnline;
}
```



### Custom Hook 사용하기

```react
function UserStatus(props) {
    const isOnline = useUserStatus(props.user.id);
    
    if (isONline === null) {
        return '대기중...';
    }
    
    return isOnline? '온라인' : '오프라인';
}

function UserListItem(props) {
    const isOnline = useUserStatus(props.user.id);
    
    return (
    	<li style={{ color: isOnline ? 'green' : 'black' }}>
        	{props.user.name}
        </li>
    )
}
```



- **Custom Hook**의 이름은 꼭 **use**로 시작해야한다
- 여러 개의 컴포넌트에서 하나의 Custom Hook을 사용할 때 컴포넌트 내부의 모든 state와 effects들은 전부 분리되어 있다 => 같은 Custom Hook을 쓰는 컴포넌트끼리의 공유되는 부분은 없다
- Custom Hook이 state을 분리하는가? => No, 리액트 컴포넌트 각각의 Custom Hook 호출에 대해서 분리된 state를 얻게 됨
- 각 Custom Hook의 호출 또한 완전히 독립적이다(일반적인 Hook처럼)



### Hook들끼리 데이터를 공유하는 방법

- 

